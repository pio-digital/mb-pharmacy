from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from home.forms import ItemTransaksiFormSet, TransaksiCreateForm
from home.models import Transaksi


@login_required(login_url="/accounts/login/")
def index(request):

    # Page from the theme
    return render(request, "pages/index.html")


@login_required(login_url="/accounts/login/")
def pos_page(request):
    context = {
        "segment": "pos_page",
    }
    return render(request, "pages/pos.html", context)


class POSView(LoginRequiredMixin, CreateView):
    login_url = "login"
    redirect_field_name = "home"
    model = Transaksi
    template_name = "pages/pos.html"
    form_class = TransaksiCreateForm
    success_url = reverse_lazy("pos_page")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
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
