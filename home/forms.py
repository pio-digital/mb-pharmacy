from django import forms

from home.consts import STATUS_CHOICES
from home.models import ItemTransaksi, Lokasi, MetodePembayaran, Transaksi


class TransaksiCreateForm(forms.ModelForm):
    metode_pembayaran = forms.ModelChoiceField(
        queryset=MetodePembayaran.objects.all(),
        widget=forms.Select(attrs={"class": "form-control form-control-md"}),
    )
    total_biaya = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class": "form-control form-control-md",
                "placeholder": "Price",
                "style": "background: transparent; border: none;",
                "disabled": True,
            }
        )
    )
    status = forms.ChoiceField(
        choices=STATUS_CHOICES,
        widget=forms.Select(attrs={"class": "form-control form-control-md"}),
    )
    lokasi = forms.ModelChoiceField(
        queryset=Lokasi.objects.all(),
        widget=forms.Select(attrs={"class": "form-control form-control-md"}),
        initial=Lokasi.objects.first(),
    )

    class Meta:
        model = Transaksi
        exclude = (
            "uid",
            "profile",
        )


class ItemTransaksiForm(forms.ModelForm):
    class Meta:
        model = ItemTransaksi
        exclude = (
            "uid",
            "transaksi",
        )


ItemTransaksiFormSet = forms.inlineformset_factory(
    Transaksi,
    ItemTransaksi,
    form=ItemTransaksiForm,
    extra=2,
)
