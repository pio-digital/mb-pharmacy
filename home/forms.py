from dal import autocomplete
from django import forms

from home.consts import STATUS_CHOICES
from home.models import (
    ItemTransaksi,
    MetodePembayaran,
    Pembayaran,
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
            "nama_obat": forms.HiddenInput(),
            "tanggal_kedaluwarsa": forms.DateInput(
                attrs={"type": "date", "class": "form-control"}
            ),
            "harga": forms.TextInput(
                attrs={
                    "@change.debounce": "changeHarga($event)",
                    # "x-mask:dynamic": "$money($input, '.', ',')"
                }
            ),
            "diskon": forms.TextInput(
                attrs={"@change.debounce": "changeDiskon($event)"}
            ),
            "nominal_diskon": forms.TextInput(attrs={"readonly": "true"}),
        }


class PembelianForm(forms.ModelForm):
    class Meta:
        model = Pembelian
        fields = "__all__"
        widgets = {
            "nomor_pre_order": forms.TextInput(attrs={"readonly": "true"}),
            "diskon": forms.NumberInput(
                attrs={
                    "x-model": "diskon",
                    "x-on:change.debounce": "updateDiskon($event)",
                    "x-on:keydown.debounce": "updateDiskon($event)",
                }
            ),
            "pajak": forms.NumberInput(
                attrs={
                    "x-model": "pajak",
                    "x-on:change.debounce": "updatePajak($event)",
                }
            ),
            "total": forms.NumberInput(
                attrs={
                    "x-model": "total",
                    "readonly": "true",
                    "x-money.en-US.USD": "total",
                }
            ),
            "nominal_pajak": forms.NumberInput(
                attrs={"x-model": "nominal_pajak", "readonly": "true"}
            ),
            "nominal_diskon": forms.NumberInput(
                attrs={"x-model": "nominal_diskon", "readonly": "true"}
            ),
            "tanggal_faktur": forms.DateInput(
                attrs={"type": "date", "class": "form-control"}
            ),
            "tanggal_jatuh_tempo": forms.DateInput(
                attrs={"type": "date", "class": "form-control"}
            ),
        }


class VarianProdukForm(forms.ModelForm):
    class Meta:
        model = VarianProduk
        fields = "__all__"
        widgets = {
            "persentase_margin": forms.NumberInput(
                attrs={"onchange": "updateHargaJual(this)"}
            ),
            "nominal_margin": forms.NumberInput(
                attrs={"onchange": "updateNominal(this)"}
            ),
            "harga_jual": forms.NumberInput(
                attrs={"onchange": "updatePersentaseMargin(this)"}
            ),
            "tanggal_kedaluwarsa": forms.DateInput(
                attrs={"type": "date", "class": "form-control"}
            ),
        }
        labels = {
            "persentase_margin": "Margin (%)",
            "nominal_margin": "Margin (Rp)",
            "tanggal_kedaluwarsa": "Tgl. kedaluwarsa",
            "kuantitas": "Qty",
            "sku": "SKU",
        }


class PembayaranForm(forms.ModelForm):
    class Meta:
        model = Pembayaran
        fields = "__all__"
        widgets = {
            "tanggal": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
        }
