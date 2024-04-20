from dal import autocomplete
from django.urls import path

from home.models import Produk


class ProdukAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return Produk.objects.none()

        qs = Produk.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs


urls = [
    path(
        "produk-autocomplete/",
        ProdukAutocomplete.as_view(),
        name="produk-autocomplete",
    ),
]
