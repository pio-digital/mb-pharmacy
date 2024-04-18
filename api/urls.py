from django.urls import re_path
from django.views.decorators.csrf import csrf_exempt

from api import views

urlpatterns = [
    re_path("unit/((?P<pk>\d+)/)?", csrf_exempt(views.UnitView.as_view())),
    re_path("supplier/((?P<pk>\d+)/)?", csrf_exempt(views.SupplierView.as_view())),
    re_path("produk/((?P<pk>\d+)/)?", csrf_exempt(views.ProdukView.as_view())),
    re_path("lokasi/((?P<pk>\d+)/)?", csrf_exempt(views.LokasiView.as_view())),
    re_path(
        "metodepembayaran/((?P<pk>\d+)/)?",
        csrf_exempt(views.MetodePembayaranView.as_view()),
    ),
    re_path("transaksi/((?P<pk>\d+)/)?", csrf_exempt(views.TransaksiView.as_view())),
    re_path(
        "itemtransaksi/((?P<pk>\d+)/)?", csrf_exempt(views.ItemTransaksiView.as_view())
    ),
    re_path("sumberdana/((?P<pk>\d+)/)?", csrf_exempt(views.SumberDanaView.as_view())),
    re_path("varian/((?P<pk>\d+)/)?", csrf_exempt(views.VarianProdukView.as_view())),
]
