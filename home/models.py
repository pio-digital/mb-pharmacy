# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Unit(models.Model):

    #__Unit_FIELDS__
    nama = models.CharField(max_length=255, null=True, blank=True)

    #__Unit_FIELDS__END

    class Meta:
        verbose_name        = _("Unit")
        verbose_name_plural = _("Unit")


class Supplier(models.Model):

    #__Supplier_FIELDS__
    nama = models.CharField(max_length=255, null=True, blank=True)
    nomor_kontak = models.CharField(max_length=255, null=True, blank=True)

    #__Supplier_FIELDS__END

    class Meta:
        verbose_name        = _("Supplier")
        verbose_name_plural = _("Supplier")


class Produk(models.Model):

    #__Produk_FIELDS__
    supplier = models.CharField(max_length=255, null=True, blank=True)
    nama = models.CharField(max_length=255, null=True, blank=True)
    brand = models.CharField(max_length=255, null=True, blank=True)
    kemasan = models.CharField(max_length=255, null=True, blank=True)
    deskripsi = models.CharField(max_length=255, null=True, blank=True)

    #__Produk_FIELDS__END

    class Meta:
        verbose_name        = _("Produk")
        verbose_name_plural = _("Produk")


class Akun(models.Model):

    #__Akun_FIELDS__
    role = models.CharField(max_length=255, null=True, blank=True)
    user = models.CharField(max_length=255, null=True, blank=True)

    #__Akun_FIELDS__END

    class Meta:
        verbose_name        = _("Akun")
        verbose_name_plural = _("Akun")


class Lokasi(models.Model):

    #__Lokasi_FIELDS__
    nama_toko = models.CharField(max_length=255, null=True, blank=True)
    alamat_lengkap = models.CharField(max_length=255, null=True, blank=True)
    nomor_telepon = models.CharField(max_length=255, null=True, blank=True)

    #__Lokasi_FIELDS__END

    class Meta:
        verbose_name        = _("Lokasi")
        verbose_name_plural = _("Lokasi")


class Metodepembayaran(models.Model):

    #__Metodepembayaran_FIELDS__
    nama = models.CharField(max_length=255, null=True, blank=True)

    #__Metodepembayaran_FIELDS__END

    class Meta:
        verbose_name        = _("Metodepembayaran")
        verbose_name_plural = _("Metodepembayaran")


class Transaksi(models.Model):

    #__Transaksi_FIELDS__
    akun = models.CharField(max_length=255, null=True, blank=True)
    lokasi = models.CharField(max_length=255, null=True, blank=True)
    metode_pembayaran = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)

    #__Transaksi_FIELDS__END

    class Meta:
        verbose_name        = _("Transaksi")
        verbose_name_plural = _("Transaksi")


class Itemtransaksi(models.Model):

    #__Itemtransaksi_FIELDS__
    transaksi = models.CharField(max_length=255, null=True, blank=True)
    item = models.CharField(max_length=255, null=True, blank=True)
    tipe_transaksi = models.CharField(max_length=255, null=True, blank=True)

    #__Itemtransaksi_FIELDS__END

    class Meta:
        verbose_name        = _("Itemtransaksi")
        verbose_name_plural = _("Itemtransaksi")


class Sumberdana(models.Model):

    #__Sumberdana_FIELDS__
    nama = models.CharField(max_length=255, null=True, blank=True)

    #__Sumberdana_FIELDS__END

    class Meta:
        verbose_name        = _("Sumberdana")
        verbose_name_plural = _("Sumberdana")


class Varianproduk(models.Model):

    #__Varianproduk_FIELDS__
    barcode = models.CharField(max_length=255, null=True, blank=True)
    sku = models.CharField(max_length=255, null=True, blank=True)
    tanggal_kedaluwarsa = models.CharField(max_length=255, null=True, blank=True)
    unit = models.CharField(max_length=255, null=True, blank=True)
    margin = models.CharField(max_length=255, null=True, blank=True)
    nama_rak = models.CharField(max_length=255, null=True, blank=True)

    #__Varianproduk_FIELDS__END

    class Meta:
        verbose_name        = _("Varianproduk")
        verbose_name_plural = _("Varianproduk")



#__MODELS__END
