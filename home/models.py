import random
import string
from datetime import date

from bson import objectid
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _

from helpers.util import format_currency
from home.consts import (
    CASHIER,
    CURRENCY_CHOICES,
    CURRENCY_IDR,
    NON_PRESCRIPTION,
    PENDING,
    ROLE_CHOICES,
    STATUS_CHOICES,
    SUCCESS,
    TRANSACTION_TYPE_CHOICES,
    VOID,
)


def create_object_id():
    return str(objectid.ObjectId())


def generate_sku(length=12):
    characters = string.ascii_uppercase + string.digits
    return "".join(random.choices(characters, k=length))


def generate_faktur(length=9):
    digits = string.digits
    return "".join(random.choices(digits, k=length))


def generate_nomor_pre_order(id: int = 0):
    today_date = date.today().isoformat().replace("-", "")

    return f"PO{today_date}.{id}"


class BaseModel(models.Model):
    uid = models.CharField(default=create_object_id, db_index=True, max_length=32)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ["-uid"]


class UserProfile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(
        max_length=15,
        choices=ROLE_CHOICES,
        default=CASHIER,
    )

    class Meta:
        verbose_name = _("User Profile")
        verbose_name_plural = _("User Profile")

    def __str__(self):
        return f"{self.user} - {self.role}"


# __MODELS__
class Unit(BaseModel):

    # __Unit_FIELDS__
    nama = models.CharField(max_length=30)

    # __Unit_FIELDS__END

    class Meta:
        verbose_name = _("Unit")
        verbose_name_plural = _("Unit")

    def __str__(self):
        return self.nama


class Supplier(BaseModel):

    # __Supplier_FIELDS__
    nama = models.CharField(max_length=50)
    nomor_kontak = models.CharField(max_length=15, null=True, blank=True)

    # __Supplier_FIELDS__END

    class Meta:
        verbose_name = _("Supplier")
        verbose_name_plural = _("Supplier")

    def __str__(self):
        return self.nama


class Produk(BaseModel):

    # __Produk_FIELDS__
    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE,
    )
    nama = models.CharField(max_length=50, null=True, blank=True)
    brand = models.CharField(max_length=50, null=True, blank=True)
    kemasan = models.CharField(max_length=32, null=True, blank=True)
    unit_per_kemasan = models.PositiveIntegerField()
    deskripsi = models.TextField(blank=True, null=True)

    # __Produk_FIELDS__END

    class Meta:
        verbose_name = _("Produk")
        verbose_name_plural = _("Produk")

    def __str__(self):
        return self.nama


class VarianProduk(BaseModel):

    # __Varianproduk_FIELDS__
    produk = models.ForeignKey(Produk, on_delete=models.CASCADE)
    barcode = models.CharField(max_length=32, null=True, blank=True)
    sku = models.CharField(
        max_length=32,
        default=generate_sku,
    )
    tanggal_kedaluwarsa = models.DateField()
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    kuantitas = models.PositiveIntegerField()
    harga_beli = models.PositiveIntegerField()
    kurs_harga_beli = models.CharField(
        max_length=3, default=CURRENCY_IDR, choices=CURRENCY_CHOICES
    )
    harga_jual = models.PositiveIntegerField()
    kurs_harga_jual = models.CharField(
        max_length=3, default=CURRENCY_IDR, choices=CURRENCY_CHOICES
    )
    margin = models.CharField(max_length=255, null=True, blank=True)
    nama_rak = models.CharField(max_length=30, null=True, blank=True)

    # __Varianproduk_FIELDS__END

    class Meta:
        verbose_name = _("Varian")
        verbose_name_plural = _("Varian")

    def __str__(self) -> str:
        return f"{self.sku} {self.produk}: {self.unit}"


class Lokasi(BaseModel):

    # __Lokasi_FIELDS__
    nama_toko = models.CharField(max_length=255, null=True, blank=True)
    alamat_lengkap = models.CharField(max_length=255, null=True, blank=True)
    nomor_telepon = models.CharField(max_length=255, null=True, blank=True)

    # __Lokasi_FIELDS__END

    class Meta:
        verbose_name = _("Lokasi")
        verbose_name_plural = _("Lokasi")

    def __str__(self):
        return self.nama_toko


class MetodePembayaran(BaseModel):

    # __Metodepembayaran_FIELDS__
    nama = models.CharField(max_length=255, null=True, blank=True)

    # __Metodepembayaran_FIELDS__END

    class Meta:
        verbose_name = _("Metode Pembayaran")
        verbose_name_plural = _("Metode Pembayaran")

    def __str__(self):
        return self.nama


class Transaksi(BaseModel):
    class StatusChoices(models.TextChoices):
        SUCCESS = "success", _("Sukses")
        PENDING = "pending", _("Tertunda")
        CANCELLED = "cancelled", _("Dibatalkan")
        VOID = "void", _("Void")

    # __Transaksi_FIELDS__
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    lokasi = models.ForeignKey(
        Lokasi,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    kurs = models.CharField(
        max_length=3, default=CURRENCY_IDR, choices=CURRENCY_CHOICES
    )
    total_biaya = models.IntegerField()
    metode_pembayaran = models.ForeignKey(
        MetodePembayaran,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=PENDING,
    )

    # __Transaksi_FIELDS__END

    class Meta:
        verbose_name = _("Transaksi")
        verbose_name_plural = _("Transaksi")

    def __str__(self):
        return f"{self.profile} – {self.lokasi} {format_currency(self.total_biaya, self.kurs)}"


class ItemTransaksi(BaseModel):
    # __ItemTransaksi_FIELDS__
    transaksi = models.ForeignKey(Transaksi, on_delete=models.CASCADE)
    item = models.ForeignKey(
        VarianProduk,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    kuantitas = models.PositiveIntegerField()
    kurs = models.CharField(
        max_length=3, default=CURRENCY_IDR, choices=CURRENCY_CHOICES
    )
    harga = models.IntegerField()
    tipe_transaksi = models.CharField(
        max_length=15,
        choices=TRANSACTION_TYPE_CHOICES,
        default=NON_PRESCRIPTION,
    )

    # __ItemTransaksi_FIELDS__END

    class Meta:
        verbose_name = _("Item")
        verbose_name_plural = _("Item")

    def __str__(self):
        return (
            f"{self.item} @ {self.kuantitas} {format_currency(self.harga, self.kurs)}"
        )


class SumberDana(BaseModel):

    # __SumberDana_FIELDS__
    nama = models.CharField(max_length=255, null=True, blank=True)

    # __SumberDana_FIELDS__END

    class Meta:
        verbose_name = _("Sumber Dana")
        verbose_name_plural = _("Sumber Dana")

    def __str__(self):
        return self.nama


class Pembelian(BaseModel):
    nomor_pre_order = models.TextField(blank=True, null=True)
    nomor_faktur = models.CharField(max_length=12, default=generate_faktur)
    tanggal_faktur = models.DateField()
    supplier = models.ForeignKey(
        Supplier, on_delete=models.SET_NULL, blank=True, null=True
    )
    sumber_dana = models.ForeignKey(
        SumberDana, on_delete=models.SET_NULL, blank=True, null=True
    )
    pajak = models.FloatField(blank=True, null=True)
    nominal_pajak = models.FloatField(blank=True, null=True)
    diskon = models.FloatField(blank=True, null=True)
    nominal_diskon = models.IntegerField(blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name = _("Pembelian")
        verbose_name_plural = _("Pembelian")

    def __str__(self):
        return self.nomor_pre_order


class PembelianObat(BaseModel):
    pembelian = models.ForeignKey(Pembelian, on_delete=models.CASCADE)
    obat = models.ForeignKey(Produk, on_delete=models.SET_NULL, blank=True, null=True)
    nama_obat = models.CharField(max_length=50, null=True, blank=True)
    jumlah = models.IntegerField(default=1)
    satuan = models.ForeignKey(Unit, on_delete=models.SET_NULL, blank=True, null=True)
    harga = models.IntegerField()
    diskon = models.FloatField(blank=True, null=True)
    nominal_diskon = models.IntegerField(blank=True, null=True)
    bonus = models.IntegerField(default=0)
    bonus_satuan = models.ForeignKey(
        Unit,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="bonus_satuan",
    )
    tanggal_kedaluwarsa = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name = _("Obat")
        verbose_name_plural = _("Obat")

    def __str__(self):
        if self.obat:
            return f"{self.obat}: {self.jumlah}"
        return f"{self.nama_obat}: {self.jumlah}"


class Pembayaran(BaseModel):
    tanggal = models.DateField()
    nama_pembayaran = models.CharField(max_length=50)
    nomor_transaksi = models.CharField(max_length=255, blank=True, null=True)
    total_biaya = models.IntegerField()
    sumber_dana = models.ForeignKey(
        SumberDana, on_delete=models.SET_NULL, blank=True, null=True
    )
    catatan = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = _("Pembayaran")
        verbose_name_plural = _("Pembayaran")

    def __str__(self):
        return self.nama_pembayaran


# __MODELS__END


@receiver(post_save, sender=ItemTransaksi)
def update_stock(sender, instance, created, **kwargs):
    varian_produk = instance.item

    if instance.transaksi.status == SUCCESS:
        varian_produk.kuantitas -= instance.kuantitas

    if instance.transaksi.status == VOID:
        varian_produk.kuantitas += instance.kuantitas

    varian_produk.save()


@receiver(post_save, sender=Pembelian)
def set_nomor_pre_order(sender, instance, created, **kwargs):
    if created:
        instance.nomor_pre_order = generate_nomor_pre_order(instance.pk)
        instance.save()
