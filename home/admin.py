from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from home.forms import (
    ItemTransaksiForm,
    PembayaranForm,
    PembelianForm,
    PembelianObatForm,
    VarianProdukForm,
)
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


# Resources
class TransaksiResource(resources.ModelResource):

    class Meta:
        model = Transaksi


class PembayaranResource(resources.ModelResource):

    class Meta:
        model = Pembayaran


class PembelianResource(resources.ModelResource):

    class Meta:
        model = Pembelian


# Register your models here.


class PembelianObatInline(admin.TabularInline):
    model = PembelianObat
    form = PembelianObatForm
    extra = 0
    exclude = ("uid",)

    template = "admin/pembelian/edit_inline/tabular.html"


class VarianProdukInline(admin.TabularInline):
    model = VarianProduk
    form = VarianProdukForm
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
class PembelianAdmin(ImportExportModelAdmin):
    form = PembelianForm
    search_fields = [
        "nomor_pre_order",
        "nomor_faktur",
        "supplier",
    ]
    exclude = ["uid"]
    inlines = [PembelianObatInline]

    resource_classes = [PembelianResource]

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
    list_filter = ["supplier", "sumber_dana", "tanggal_faktur"]

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
class PembayaranAdmin(ImportExportModelAdmin):
    form = PembayaranForm
    exclude = ["uid"]

    resourse_classes = [PembayaranResource]
    search_fields = [
        "nomor_transaksi",
        "nama_pembayaran",
    ]
    list_display = [
        "tanggal",
        "nomor_transaksi",
        "nama_pembayaran",
        "total_biaya",
        "sumber_dana",
    ]
    list_filter = ["sumber_dana", "tanggal"]
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
class TransaksiAdmin(ImportExportModelAdmin):
    resourse_classes = [TransaksiResource]

    list_filter = ["lokasi", "metode_pembayaran", "status", "created_on"]
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
    list_display = ["nama_toko", "alamat_lengkap", "nomor_telepon"]


@admin.register(MetodePembayaran)
class MetodePembayaranAdmin(admin.ModelAdmin):
    exclude = ["uid"]


@admin.register(SumberDana)
class SumberDanaAdmin(admin.ModelAdmin):
    exclude = ["uid"]


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    exclude = ["uid"]
    list_display = ["nama", "nama_perusahaan", "nomor_kontak"]


@admin.register(Storage)
class StorageAdmin(admin.ModelAdmin):
    exclude = ["uid"]


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    exclude = ["uid"]


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    exclude = ["uid"]
    list_display = ["user", "role"]


@admin.register(VarianProduk)
class VarianProduk(admin.ModelAdmin):
    search_fields = [
        "produk__nama",
        "barcode",
        "sku",
    ]
    list_display = [
        "produk",
        "barcode",
        "sku",
        "tanggal_kedaluwarsa",
        "unit",
        "kuantitas",
        "storage",
    ]
    list_filter = ["produk", "tanggal_kedaluwarsa", "unit", "storage"]
