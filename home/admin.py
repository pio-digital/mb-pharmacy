from django.contrib import admin

from home.forms import ItemTransaksiForm, PembelianForm, PembelianObatForm
from home.models import (
    ItemTransaksi,
    Lokasi,
    MetodePembayaran,
    Pembayaran,
    Pembelian,
    PembelianObat,
    Produk,
    Storage,
    SumberDana,
    Supplier,
    Transaksi,
    Unit,
    UserProfile,
    VarianProduk,
)

# Register your models here.


class PembelianObatInline(admin.TabularInline):
    model = PembelianObat
    form = PembelianObatForm
    extra = 0
    exclude = ("uid",)

    template = "admin/pembelian/edit_inline/tabular.html"


class VarianProdukInline(admin.TabularInline):
    model = VarianProduk
    extra = 0
    exclude = ["uid"]

    template = "admin/produk/edit_inline/tabular.html"


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

    list_display = [
        "tanggal_faktur",
        "nomor_faktur",
        "nomor_pre_order",
        "supplier",
        "pajak",
        "diskon",
        "total",
        "sumber_dana",
        "get_total_produk",
    ]

    fieldsets = [
        (
            None,
            {
                "fields": [("tanggal_faktur", "nomor_faktur", "nomor_pre_order")],
            },
        ),
        (
            None,
            {
                "fields": [("supplier", "sumber_dana", "total")],
            },
        ),
        (
            None,
            {
                "fields": [("pajak", "nominal_pajak")],
            },
        ),
        (
            None,
            {
                "fields": [("diskon", "nominal_diskon")],
            },
        ),
    ]

    change_form_template = "admin/pembelian/change_form.html"

    def get_total_produk(self, obj):
        return obj.pembelianobat_set.count()

    get_total_produk.short_description = "Total Produk"


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

    list_display = [
        "id",
        "nama",
        "brand",
        "kemasan",
        "unit_per_kemasan",
        "supplier",
        "get_total_varian",
    ]

    list_filter = ["supplier"]

    change_form_template = "admin/produk/change_form.html"

    def get_total_varian(self, obj):
        return obj.varianproduk_set.count()

    get_total_varian.short_description = "Total Varian"


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
    exclude = ["uid"]
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


@admin.register(MetodePembayaran)
class MetodePembayaranAdmin(admin.ModelAdmin):
    exclude = ["uid"]


@admin.register(SumberDana)
class SumberDanaAdmin(admin.ModelAdmin):
    exclude = ["uid"]


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    exclude = ["uid"]


@admin.register(Storage)
class StorageAdmin(admin.ModelAdmin):
    exclude = ["uid"]


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    exclude = ["uid"]


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    exclude = ["uid"]
