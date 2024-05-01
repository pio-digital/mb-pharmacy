from django.urls import re_path
from django.views.decorators.csrf import csrf_exempt

from api.views import *

urlpatterns = [
    re_path("unit/((?P<pk>\d+)/)?", csrf_exempt(UnitView.as_view())),
    re_path("supplier/((?P<pk>\d+)/)?", csrf_exempt(SupplierView.as_view())),
    re_path("produk/((?P<pk>\d+)/)?", csrf_exempt(ProdukView.as_view())),
    re_path("lokasi/((?P<pk>\d+)/)?", csrf_exempt(LokasiView.as_view())),
    re_path(
        "metodepembayaran/((?P<pk>\d+)/)?", csrf_exempt(MetodePembayaranView.as_view())
    ),
    re_path("transaksi/((?P<pk>\d+)/)?", csrf_exempt(TransaksiView.as_view())),
    re_path("itemtransaksi/((?P<pk>\d+)/)?", csrf_exempt(ItemTransaksiView.as_view())),
    re_path("sumberdana/((?P<pk>\d+)/)?", csrf_exempt(SumberDanaView.as_view())),
    re_path("varian/((?P<pk>\d+)/)?", csrf_exempt(VarianProdukView.as_view())),
    re_path("order/((?P<pk>\d+)/)?", csrf_exempt(PembelianView.as_view())),
    re_path("obat/((?P<pk>\d+)/)?", csrf_exempt(PembelianObatView.as_view())),
    re_path("operasional/((?P<pk>\d+)/)?", csrf_exempt(PembayaranView.as_view())),
    re_path("storage/((?P<pk>\d+)/)?", csrf_exempt(StorageView.as_view())),
]
