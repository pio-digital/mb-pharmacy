from datetime import date, timedelta

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.db.models.functions import Coalesce
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, TemplateView

from helpers.util import format_currency
from home.consts import CURRENCY_IDR, SUCCESS
from home.forms import TransaksiCreateForm
from home.models import ItemTransaksi, Produk, Supplier, Transaksi, VarianProduk


class HomeView(LoginRequiredMixin, View):
    login_url = "login"
    redirect_field_name = "home"

    def get(self, request, *args, **kwargs):
        today = date.today()
        two_month = today + timedelta(days=60)
        context = {
            "cash": format_currency(
                Transaksi.objects.filter(
                    metode_pembayaran_id=1,
                    status=SUCCESS,
                    created_on__date=date.today(),
                )
                .aggregate(total=Coalesce(Sum("total_biaya"), 0))
                .get("total", 0),
                CURRENCY_IDR,
            ),
            "total_products": Produk.objects.count(),
            "total_suppliers": Supplier.objects.count(),
            "best_selling": ItemTransaksi.objects.values("item__produk__nama")
            .annotate(sold=Sum("item"))
            .order_by("-sold")[:5],
            "empties": VarianProduk.objects.filter(kuantitas__lte=10).order_by(
                "-kuantitas"
            ),
            "expireds": VarianProduk.objects.filter(
                tanggal_kedaluwarsa__range=(today, two_month)
            ).order_by("-tanggal_kedaluwarsa"),
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

        # if self.request.POST:
        #     context["formset"] = ItemTransaksiFormSet(
        #         self.request.POST, instance=self.object
        #     )
        # else:
        #     context["formset"] = ItemTransaksiFormSet(instance=self.object)
        return context

    # def get_success_url(self) -> str:
    #     messages.add_message(
    #         self.request,
    #         messages.SUCCESS,
    #         f"Transaksi {self.object} berhasil!",
    #     )
    #     return super().get_success_url()

    # def form_valid(self, form):
    #     context = self.get_context_data()
    #     formset = context["formset"]
    #     with transaction.atomic():
    #         form.instance.profile = self.request.user.userprofile
    #         self.object = form.save()
    #         if formset.is_valid():
    #             formset.instance = self.object
    #             formset.save()
    #     return super().form_valid(form)


class ReportView(LoginRequiredMixin, TemplateView):
    login_url = "login"
    redirect_field_name = "home"
    template_name = "pages/report.html"
    model = VarianProduk
    fields = ""

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["segment"] = "sales_report_page"

        return context
