from rest_framework import serializers

try:

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
        VarianProduk,
    )

except:
    pass


class UnitSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = Unit
        except:
            pass
        fields = "__all__"


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = Supplier
        except:
            pass
        fields = "__all__"


class ProdukSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = Produk
        except:
            pass
        fields = "__all__"


class LokasiSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = Lokasi
        except:
            pass
        fields = "__all__"


class MetodePembayaranSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = MetodePembayaran
        except:
            pass
        fields = "__all__"


class TransaksiSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = Transaksi
        except:
            pass
        fields = "__all__"


class ItemTransaksiSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = ItemTransaksi
        except:
            pass
        fields = "__all__"


class SumberDanaSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = SumberDana
        except:
            pass
        fields = "__all__"


class VarianProdukSerializer(serializers.ModelSerializer):
    produk = ProdukSerializer()
    unit = UnitSerializer()

    class Meta:

        try:
            model = VarianProduk
        except:
            pass
        fields = "__all__"


class PembelianSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = Pembelian
        except:
            pass
        fields = "__all__"


class PembelianObatSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = PembelianObat
        except:
            pass
        fields = "__all__"


class PembayaranSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = Pembayaran
        except:
            pass
        fields = "__all__"


class StorageSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = Storage
        except:
            pass
        fields = "__all__"
