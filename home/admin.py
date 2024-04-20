from django.apps import apps
from django.contrib import admin

from home.forms import ItemTransaksiForm, PembelianForm, PembelianObatForm
from home.models import (
    ItemTransaksi,
    Lokasi,
    Pembayaran,
    Pembelian,
    PembelianObat,
    Produk,
    Transaksi,
    VarianProduk,
)

# Register your models here.


class PembelianObatInline(admin.TabularInline):
    model = PembelianObat
    form = PembelianObatForm
    extra = 1
    exclude = ("uid",)


class VarianProdukInline(admin.TabularInline):
    model = VarianProduk
    extra = 1
    exclude = ["uid", "kurs_harga_beli", "kurs_harga_jual"]


class ItemTransaksiInline(admin.TabularInline):
    model = ItemTransaksi
    form = ItemTransaksiForm
    max_num = 0
    can_delete = False
    readonly_fields = ["item", "kuantitas", "harga", "tipe_transaksi"]


@admin.register(Pembelian)
class PembelianAdmin(admin.ModelAdmin):
    form = PembelianForm
    search_fields = [
        "nomor_pre_order",
        "nomor_faktur",
        "supplier",
    ]
    exclude = ["uid"]
    inlines = [PembelianObatInline]


@admin.register(Pembayaran)
class PembayaranAdmin(admin.ModelAdmin):
    exclude = ["uid"]
    search_fields = [
        "nomor_transaksi",
        "nama_pembayaran",
    ]
    fieldsets = [
        (
            None,
            {
                "fields": [("tanggal", "nomor_transaksi")],
            },
        ),
        (
            None,
            {
                "fields": [("nama_pembayaran", "total_biaya", "sumber_dana")],
            },
        ),
        (
            None,
            {
                "fields": ["catatan"],
            },
        ),
    ]


@admin.register(Produk)
class ProdukAdmin(admin.ModelAdmin):
    search_fields = [
        "nama",
    ]
    exclude = ["uid"]
    inlines = [VarianProdukInline]
    fieldsets = [
        (
            None,
            {
                "fields": ["supplier"],
            },
        ),
        (
            None,
            {
                "fields": [("nama", "brand")],
            },
        ),
        (
            None,
            {
                "fields": [("kemasan", "unit_per_kemasan")],
            },
        ),
        (
            None,
            {
                "fields": ["deskripsi"],
            },
        ),
    ]


@admin.register(Transaksi)
class TransaksiAdmin(admin.ModelAdmin):
    list_filter = ["lokasi", "metode_pembayaran", "status"]
    list_display = [
        "profile",
        "created_on",
        "total_biaya",
        "metode_pembayaran",
        "status",
    ]
    exclude = ["uid", "kurs"]
    inlines = [ItemTransaksiInline]
    readonly_fields = [
        "created_on",
        "status",
        "profile",
        "lokasi",
        "total_biaya",
        "metode_pembayaran",
    ]

    fieldsets = [
        (
            None,
            {
                "fields": [
                    ("created_on", "status", "total_biaya", "metode_pembayaran")
                ],
            },
        ),
        (
            "Kasir & Toko",
            {
                "fields": [("profile", "lokasi")],
            },
        ),
    ]


@admin.register(Lokasi)
class LokasiAdmin(admin.ModelAdmin):
    exclude = ["uid"]


app_models = apps.get_app_config("home").get_models()
for model in app_models:
    try:

        # Special processing for UserProfile
        if "UserProfile" == model.__name__:

            # The model is registered only if has specific data
            # 1 -> ID
            # 2 -> User (one-to-one) relation
            if len(model._meta.fields) > 2:
                admin.site.register(model)

        # Register to Admin
        else:
            if model.__name__ not in [
                "Pembelian",
                "PembelianObat",
                "VarianProduk",
                "ItemTransaksi",
            ]:
                admin.site.register(model)

    except Exception:
        pass
