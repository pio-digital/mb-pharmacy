from rest_framework import serializers

try:

    from home.models import (
        ItemTransaksi,
        Lokasi,
        MetodePembayaran,
        Produk,
        SumberDana,
        Supplier,
        Transaksi,
        Unit,
        VarianProduk,
    )
except Exception:
    pass


class UnitSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = Unit
        except Exception:
            pass
        fields = "__all__"


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = Supplier
        except Exception:
            pass
        fields = "__all__"


class ProdukSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = Produk
        except Exception:
            pass
        fields = "__all__"


class LokasiSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = Lokasi
        except Exception:
            pass
        fields = "__all__"


class MetodePembayaranSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = MetodePembayaran
        except Exception:
            pass
        fields = "__all__"


class TransaksiSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = Transaksi
        except Exception:
            pass
        fields = "__all__"


class ItemTransaksiSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = ItemTransaksi
        except Exception:
            pass
        fields = "__all__"


class SumberDanaSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = SumberDana
        except Exception:
            pass
        fields = "__all__"


class VarianProdukSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = VarianProduk
        except Exception:
            pass
        fields = "__all__"
