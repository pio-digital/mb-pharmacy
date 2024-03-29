from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, TemplateView

from home.forms import ItemTransaksiFormSet, TransaksiCreateForm
from home.models import Transaksi, VarianProduk


class HomeView(LoginRequiredMixin, View):
    login_url = "login"
    redirect_field_name = "home"

    def get(self, request, *args, **kwargs):
        return render(request, "pages/index.html")


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

        if self.request.POST:
            context["formset"] = ItemTransaksiFormSet(
                self.request.POST, instance=self.object
            )
        else:
            context["formset"] = ItemTransaksiFormSet(instance=self.object)
        return context

    def get_success_url(self) -> str:
        messages.add_message(
            self.request,
            messages.SUCCESS,
            f"Transaksi {self.object} berhasil!",
        )
        return super().get_success_url()

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context["formset"]
        with transaction.atomic():
            form.instance.profile = self.request.user.userprofile
            self.object = form.save()
            if formset.is_valid():
                formset.instance = self.object
                formset.save()
        return super().form_valid(form)


class SearchView(TemplateView):
    model = VarianProduk
    template_name = "pages/pos.html"

    def get(self, request, *args, **kwargs):
        q = request.GET.get("q", "")
        self.results = VarianProduk.objects.filter(
            Q(barcode__icontains=q) | Q(produk__nama=q)
        )
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        """Add context to the template"""
        return super().get_context_data(results=self.results, **kwargs)
