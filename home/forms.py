from django import forms

from home.models import ItemTransaksi, Transaksi


class TransaksiCreateForm(forms.ModelForm):
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
