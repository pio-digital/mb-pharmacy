import django_filters as filters
from django import forms
from django_filters.widgets import SuffixedMultiWidget

from home.models import ItemTransaksi, MetodePembayaran, Transaksi


class CustomDateRangeWidget(SuffixedMultiWidget):
    template_name = "django_filters/widgets/multiwidget.html"
    suffixes = ["after", "before"]

    def __init__(self, attrs=None):
        widgets = (
            forms.DateInput(attrs={"type": "date"}),
            forms.DateInput(attrs={"type": "date"}),
        )
        super().__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return [value.start, value.stop]
        return [None, None]


class ItemTransaksiFilter(filters.FilterSet):
    date = filters.DateFromToRangeFilter(
        field_name="created_on",
        label="Rentang Tanggal",
        widget=CustomDateRangeWidget,
    )
    metode_pembayaran = filters.ModelChoiceFilter(
        queryset=MetodePembayaran.objects.all(),
        field_name="transaksi__metode_pembayaran",
        label="Metode Pembayaran",
    )
    status = filters.ChoiceFilter(
        choices=Transaksi.StatusChoices.choices,
        field_name="transaksi__status",
        label="Status",
    )

    class Meta:
        model = ItemTransaksi
        fields = [
            "metode_pembayaran",
            "status",
            "date",
        ]
