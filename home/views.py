import json
from datetime import date, timedelta

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.db.models import CharField, F, Sum, Value
from django.db.models.functions import Coalesce, Concat
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView
from django_filters.views import FilterView

from helpers.util import format_currency
from home.consts import (
    CURRENCY_IDR,
    METODE_PEMBAYARAN_BANK_TRANSFER_ID,
    METODE_PEMBAYARAN_TUNAI_ID,
    SUCCESS,
    VOID,
)
from home.filters import ItemTransaksiFilter
from home.forms import ItemTransaksiFormSet, TransaksiCreateForm
from home.models import (
    ItemTransaksi,
    Pembelian,
    Produk,
    SumberDana,
    Supplier,
    Transaksi,
    VarianProduk,
)


class HomeView(LoginRequiredMixin, View):
    login_url = "login"
    redirect_field_name = "home"

    def get(self, request, *args, **kwargs):
        today = date.today()
        two_month = today + timedelta(days=60)

        all_transaksi = Transaksi.objects.filter(
            metode_pembayaran_id__in=[
                METODE_PEMBAYARAN_TUNAI_ID,
                METODE_PEMBAYARAN_BANK_TRANSFER_ID,
            ],
            status=SUCCESS,
            created_on__date=date.today(),
        )

        cash_on_hand = SumberDana.objects.get(nama="Cash on Hand")
        context = {
            "all_transaksi": format_currency(
                all_transaksi.aggregate(total=Coalesce(Sum("total_biaya"), 0)).get(
                    "total", 0
                ),
                CURRENCY_IDR,
            ),
            "cash": format_currency(
                cash_on_hand.saldo,
                CURRENCY_IDR,
            ),
            "total_products": Produk.objects.count(),
            "total_suppliers": Supplier.objects.count(),
            "best_selling": ItemTransaksi.objects.values("item__produk__nama")
            .annotate(sold=Sum("item"))
            .order_by("-sold")[:5],
            "total_empties": VarianProduk.objects.filter(kuantitas__lte=10)
            .order_by("-kuantitas")
            .count(),
            "total_expireds": VarianProduk.objects.filter(
                tanggal_kedaluwarsa__range=(today, two_month)
            )
            .order_by("produk", "-tanggal_kedaluwarsa")
            .distinct("produk")
            .count(),
        }
        return render(request, "pages/index.html", context)


class POSView(LoginRequiredMixin, CreateView):
    login_url = "login"
    redirect_field_name = "home"
    model = Transaksi
    template_name = "pages/pos.html"
    form_class = TransaksiCreateForm
    success_url = reverse_lazy("pos_page")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["segment"] = "pos_page"
        context["variant"] = VarianProduk.objects.all()

        if self.request.POST:
            context["formset"] = ItemTransaksiFormSet(
                self.request.POST, instance=self.object
            )
        else:
            context["formset"] = ItemTransaksiFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context["formset"]
        with transaction.atomic():
            form.instance.profile = self.request.user.userprofile
            form.instance.lokasi_id = 1
            self.object = form.save()

            # Set ItemTransaksi
            products = json.loads(formset.data.get("products"))

            for product in products:
                ItemTransaksi.objects.create(
                    transaksi=self.object,
                    item_id=product.get("item"),
                    kuantitas=product.get("kuantitas"),
                    harga=product.get("harga"),
                    tipe_transaksi=product.get("tipe_transaksi"),
                )

        return super().form_valid(form)


class ReportView(LoginRequiredMixin, FilterView):
    login_url = "login"
    redirect_field_name = "home"
    model = ItemTransaksi
    filterset_class = ItemTransaksiFilter
    template_name = "pages/report.html"
    context_object_name = "transaksi"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["segment"] = "sales_report_page"
        transaksi = context["transaksi"]

        transaksi = transaksi.values("item").annotate(
            nama=Concat(
                F("item__produk__nama"),
                Value(": "),
                F("item__unit__nama"),
                output_field=CharField(),
            ),
            amount=Sum(F("harga")),
        )

        context["labels"] = ", ".join([x["nama"] for x in transaksi])
        context["data"] = [x["amount"] for x in transaksi]
        context["total_pemasukkan"] = format_currency(
            transaksi.aggregate(total=Coalesce(Sum("harga"), 0)).get("total", 0),
            CURRENCY_IDR,
        )

        # Drop some money
        success_cash_trx = (
            Transaksi.objects.filter(
                metode_pembayaran_id=METODE_PEMBAYARAN_TUNAI_ID,
                status=SUCCESS,
            )
            .aggregate(total=Coalesce(Sum("total_biaya"), 0))
            .get("total", 0)
        )
        success_account_trx = (
            Transaksi.objects.filter(
                metode_pembayaran_id=METODE_PEMBAYARAN_BANK_TRANSFER_ID,
                status=SUCCESS,
            )
            .aggregate(total=Coalesce(Sum("total_biaya"), 0))
            .get("total", 0)
        )

        void_cash_trx = (
            Transaksi.objects.filter(
                metode_pembayaran_id=METODE_PEMBAYARAN_TUNAI_ID,
                status=VOID,
            )
            .aggregate(total=Coalesce(Sum("total_biaya"), 0))
            .get("total", 0)
        )
        void_account_trx = (
            Transaksi.objects.filter(
                metode_pembayaran_id=METODE_PEMBAYARAN_BANK_TRANSFER_ID,
                status=VOID,
            )
            .aggregate(total=Coalesce(Sum("total_biaya"), 0))
            .get("total", 0)
        )

        context["cash"] = format_currency(
            success_cash_trx - void_cash_trx,
            CURRENCY_IDR,
        )
        context["rekening"] = format_currency(
            success_account_trx - void_account_trx,
            CURRENCY_IDR,
        )

        order_hutang = Pembelian.objects.filter(sumber_dana_id=3)
        context["hutang"] = format_currency(
            order_hutang.aggregate(total=Coalesce(Sum("total"), 0)).get("total", 0),
            CURRENCY_IDR,
        )
        context["list_hutang"] = order_hutang.order_by("-tanggal_faktur")

        return context


class ObatKedaluwarsaView(LoginRequiredMixin, FilterView):
    login_url = "login"
    redirect_field_name = "home"
    model = VarianProduk
    template_name = "pages/obat_page.html"
    context_object_name = "produk"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["segment"] = "obat_kedaluwarsa_page"
        context["title"] = "Obat Kedaluwarsa"
        context["is_expired"] = True

        today = date.today()
        two_month = today + timedelta(days=60)

        context["produk"] = (
            VarianProduk.objects.filter(tanggal_kedaluwarsa__range=(today, two_month))
            .order_by("produk", "-tanggal_kedaluwarsa")
            .distinct("produk")
        )

        return context


class ObatHabisView(LoginRequiredMixin, FilterView):
    login_url = "login"
    redirect_field_name = "home"
    model = VarianProduk
    template_name = "pages/obat_page.html"
    context_object_name = "produk"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["segment"] = "obat_habis_page"
        context["title"] = "Obat Habis"
        context["is_expired"] = False

        context["produk"] = VarianProduk.objects.filter(kuantitas__lte=10).order_by(
            "produk", "-kuantitas"
        )

        return context
