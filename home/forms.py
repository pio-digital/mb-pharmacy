from dal import autocomplete
from django import forms

from home.consts import STATUS_CHOICES
from home.models import (
    ItemTransaksi,
    MetodePembayaran,
    Pembelian,
    PembelianObat,
    Produk,
    Transaksi,
    VarianProduk,
)


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

    class Meta:
        model = Transaksi
        exclude = (
            "uid",
            "profile",
            "lokasi",
        )


class ItemTransaksiForm(forms.ModelForm):
    class Meta:
        model = ItemTransaksi
        exclude = (
            "uid",
            "transaksi",
        )
        widgets = {"obat": autocomplete.ModelSelect2(url="produk-autocomplete")}


ItemTransaksiFormSet = forms.inlineformset_factory(
    Transaksi,
    ItemTransaksi,
    form=ItemTransaksiForm,
    extra=2,
)


class PembelianObatForm(forms.ModelForm):
    obat = forms.ModelChoiceField(
        queryset=Produk.objects.all(), label="Produk", required=False
    )

    class Meta:
        model = PembelianObat
        fields = "__all__"
        widgets = {
            "obat": autocomplete.ModelSelect2(url="produk-autocomplete"),
            "nama_obat": forms.HiddenInput()
        }


class PembelianForm(forms.ModelForm):
    class Meta:
        model = Pembelian
        fields = "__all__"
        widgets = {
            "nomor_pre_order": forms.TextInput(attrs={"disabled": "true"}),
            "diskon": forms.NumberInput(
                attrs={
                    "x-model": "diskon",
                    "x-on:change.debounce": "updateDiskon($event)",
                    "x-on:keydown.debounce": "updateDiskon($event)"
                }
            ),
            "pajak": forms.NumberInput(
                attrs={
                    "x-model": "pajak",
                    "x-on:change.debounce": "updatePajak($event)",
                    "x-on:keydown.debounce": "updatePajak($event)"
                }
            ),
            "total": forms.NumberInput(
                attrs={
                    "x-model": "total",
                    "disabled": "false"
                }
            ),
            "nominal_pajak": forms.NumberInput(
                attrs={
                    "x-model": "nominal_pajak",
                    "disabled": "true"
                }
            ),
            "nominal_diskon": forms.NumberInput(
                attrs={
                    "x-model": "nominal_diskon",
                    "disabled": "true"
                }
            )
        }


class VarianProdukForm(forms.ModelForm):
    class Meta:
        model = VarianProduk
        fields = "__all__"
        widgets = {
            "persentase_margin": forms.NumberInput(
                attrs={"onchange": "updateHargaJual(this)"}
            ),
            "harga_jual": forms.NumberInput(attrs={"onchange": "updateMargin(this)"}),
        }
