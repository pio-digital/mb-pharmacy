# Generated by Django 4.2.8 on 2024-04-20 17:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import home.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Lokasi",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "uid",
                    models.CharField(
                        db_index=True,
                        default=home.models.create_object_id,
                        max_length=32,
                    ),
                ),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("updated_on", models.DateTimeField(auto_now=True)),
                ("nama_toko", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "alamat_lengkap",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "nomor_telepon",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
            ],
            options={
                "verbose_name": "Lokasi",
                "verbose_name_plural": "Lokasi",
            },
        ),
        migrations.CreateModel(
            name="MetodePembayaran",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "uid",
                    models.CharField(
                        db_index=True,
                        default=home.models.create_object_id,
                        max_length=32,
                    ),
                ),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("updated_on", models.DateTimeField(auto_now=True)),
                ("nama", models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                "verbose_name": "Metode Pembayaran",
                "verbose_name_plural": "Metode Pembayaran",
            },
        ),
        migrations.CreateModel(
            name="Pembelian",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "uid",
                    models.CharField(
                        db_index=True,
                        default=home.models.create_object_id,
                        max_length=32,
                    ),
                ),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("updated_on", models.DateTimeField(auto_now=True)),
                ("nomor_pre_order", models.TextField(blank=True, null=True)),
                (
                    "nomor_faktur",
                    models.CharField(
                        default=home.models.generate_faktur, max_length=12
                    ),
                ),
                ("tanggal_faktur", models.DateField()),
                ("pajak", models.FloatField(blank=True, null=True)),
                ("nominal_pajak", models.FloatField(blank=True, null=True)),
                ("diskon", models.FloatField(blank=True, null=True)),
                ("nominal_diskon", models.IntegerField(blank=True, null=True)),
                ("total", models.IntegerField(blank=True, null=True)),
            ],
            options={
                "verbose_name": "Pembelian",
                "verbose_name_plural": "Pembelian",
            },
        ),
        migrations.CreateModel(
            name="Produk",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "uid",
                    models.CharField(
                        db_index=True,
                        default=home.models.create_object_id,
                        max_length=32,
                    ),
                ),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("updated_on", models.DateTimeField(auto_now=True)),
                ("nama", models.CharField(blank=True, max_length=50, null=True)),
                ("brand", models.CharField(blank=True, max_length=50, null=True)),
                ("kemasan", models.CharField(blank=True, max_length=32, null=True)),
                ("unit_per_kemasan", models.PositiveIntegerField()),
                ("deskripsi", models.TextField(blank=True, null=True)),
            ],
            options={
                "verbose_name": "Produk",
                "verbose_name_plural": "Produk",
            },
        ),
        migrations.CreateModel(
            name="SumberDana",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "uid",
                    models.CharField(
                        db_index=True,
                        default=home.models.create_object_id,
                        max_length=32,
                    ),
                ),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("updated_on", models.DateTimeField(auto_now=True)),
                ("nama", models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                "verbose_name": "Sumber Dana",
                "verbose_name_plural": "Sumber Dana",
            },
        ),
        migrations.CreateModel(
            name="Supplier",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "uid",
                    models.CharField(
                        db_index=True,
                        default=home.models.create_object_id,
                        max_length=32,
                    ),
                ),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("updated_on", models.DateTimeField(auto_now=True)),
                ("nama", models.CharField(max_length=50)),
                (
                    "nomor_kontak",
                    models.CharField(blank=True, max_length=15, null=True),
                ),
            ],
            options={
                "verbose_name": "Supplier",
                "verbose_name_plural": "Supplier",
            },
        ),
        migrations.CreateModel(
            name="Unit",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "uid",
                    models.CharField(
                        db_index=True,
                        default=home.models.create_object_id,
                        max_length=32,
                    ),
                ),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("updated_on", models.DateTimeField(auto_now=True)),
                ("nama", models.CharField(max_length=30)),
            ],
            options={
                "verbose_name": "Unit",
                "verbose_name_plural": "Unit",
            },
        ),
        migrations.CreateModel(
            name="VarianProduk",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "uid",
                    models.CharField(
                        db_index=True,
                        default=home.models.create_object_id,
                        max_length=32,
                    ),
                ),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("updated_on", models.DateTimeField(auto_now=True)),
                ("barcode", models.CharField(blank=True, max_length=32, null=True)),
                (
                    "sku",
                    models.CharField(default=home.models.generate_sku, max_length=32),
                ),
                ("tanggal_kedaluwarsa", models.DateField()),
                ("kuantitas", models.PositiveIntegerField()),
                ("harga_beli", models.PositiveIntegerField()),
                (
                    "kurs_harga_beli",
                    models.CharField(
                        choices=[
                            ("jpy", "jpy"),
                            ("idr", "idr"),
                            ("sgd", "sgd"),
                            ("eur", "eur"),
                            ("usd", "usd"),
                        ],
                        default="idr",
                        max_length=3,
                    ),
                ),
                ("harga_jual", models.PositiveIntegerField()),
                (
                    "kurs_harga_jual",
                    models.CharField(
                        choices=[
                            ("jpy", "jpy"),
                            ("idr", "idr"),
                            ("sgd", "sgd"),
                            ("eur", "eur"),
                            ("usd", "usd"),
                        ],
                        default="idr",
                        max_length=3,
                    ),
                ),
                ("margin", models.CharField(blank=True, max_length=255, null=True)),
                ("nama_rak", models.CharField(blank=True, max_length=30, null=True)),
                (
                    "produk",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="home.produk"
                    ),
                ),
                (
                    "unit",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="home.unit"
                    ),
                ),
            ],
            options={
                "verbose_name": "Varian",
                "verbose_name_plural": "Varian",
            },
        ),
        migrations.CreateModel(
            name="UserProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "uid",
                    models.CharField(
                        db_index=True,
                        default=home.models.create_object_id,
                        max_length=32,
                    ),
                ),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("updated_on", models.DateTimeField(auto_now=True)),
                (
                    "role",
                    models.CharField(
                        choices=[("admin", "Admin"), ("cashier", "Kasir")],
                        default="cashier",
                        max_length=15,
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "User Profile",
                "verbose_name_plural": "User Profile",
            },
        ),
        migrations.CreateModel(
            name="Transaksi",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "uid",
                    models.CharField(
                        db_index=True,
                        default=home.models.create_object_id,
                        max_length=32,
                    ),
                ),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("updated_on", models.DateTimeField(auto_now=True)),
                (
                    "kurs",
                    models.CharField(
                        choices=[
                            ("jpy", "jpy"),
                            ("idr", "idr"),
                            ("sgd", "sgd"),
                            ("eur", "eur"),
                            ("usd", "usd"),
                        ],
                        default="idr",
                        max_length=3,
                    ),
                ),
                ("total_biaya", models.IntegerField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("success", "Sukses"),
                            ("pending", "Tertunda"),
                            ("cancelled", "Dibatalkan"),
                            ("void", "Void"),
                        ],
                        default="pending",
                        max_length=10,
                    ),
                ),
                (
                    "lokasi",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="home.lokasi",
                    ),
                ),
                (
                    "metode_pembayaran",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="home.metodepembayaran",
                    ),
                ),
                (
                    "profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="home.userprofile",
                    ),
                ),
            ],
            options={
                "verbose_name": "Transaksi",
                "verbose_name_plural": "Transaksi",
            },
        ),
        migrations.AddField(
            model_name="produk",
            name="supplier",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="home.supplier"
            ),
        ),
        migrations.CreateModel(
            name="PembelianObat",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "uid",
                    models.CharField(
                        db_index=True,
                        default=home.models.create_object_id,
                        max_length=32,
                    ),
                ),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("updated_on", models.DateTimeField(auto_now=True)),
                ("nama_obat", models.CharField(blank=True, max_length=50, null=True)),
                ("jumlah", models.IntegerField(default=1)),
                ("harga", models.IntegerField()),
                ("diskon", models.FloatField(blank=True, null=True)),
                ("nominal_diskon", models.IntegerField(blank=True, null=True)),
                ("bonus", models.IntegerField(default=0)),
                ("tanggal_kedaluwarsa", models.DateField(blank=True, null=True)),
                (
                    "bonus_satuan",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="bonus_satuan",
                        to="home.unit",
                    ),
                ),
                (
                    "obat",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="home.produk",
                    ),
                ),
                (
                    "pembelian",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="home.pembelian"
                    ),
                ),
                (
                    "satuan",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="home.unit",
                    ),
                ),
            ],
            options={
                "verbose_name": "Obat",
                "verbose_name_plural": "Obat",
            },
        ),
        migrations.AddField(
            model_name="pembelian",
            name="sumber_dana",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="home.sumberdana",
            ),
        ),
        migrations.AddField(
            model_name="pembelian",
            name="supplier",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="home.supplier",
            ),
        ),
        migrations.CreateModel(
            name="Pembayaran",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "uid",
                    models.CharField(
                        db_index=True,
                        default=home.models.create_object_id,
                        max_length=32,
                    ),
                ),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("updated_on", models.DateTimeField(auto_now=True)),
                ("tanggal", models.DateField()),
                ("nama_pembayaran", models.CharField(max_length=50)),
                (
                    "nomor_transaksi",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("total_biaya", models.IntegerField()),
                ("catatan", models.TextField(blank=True, null=True)),
                (
                    "sumber_dana",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="home.sumberdana",
                    ),
                ),
            ],
            options={
                "verbose_name": "Pembayaran",
                "verbose_name_plural": "Pembayaran",
            },
        ),
        migrations.CreateModel(
            name="ItemTransaksi",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "uid",
                    models.CharField(
                        db_index=True,
                        default=home.models.create_object_id,
                        max_length=32,
                    ),
                ),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("updated_on", models.DateTimeField(auto_now=True)),
                ("kuantitas", models.PositiveIntegerField()),
                (
                    "kurs",
                    models.CharField(
                        choices=[
                            ("jpy", "jpy"),
                            ("idr", "idr"),
                            ("sgd", "sgd"),
                            ("eur", "eur"),
                            ("usd", "usd"),
                        ],
                        default="idr",
                        max_length=3,
                    ),
                ),
                ("harga", models.IntegerField()),
                (
                    "tipe_transaksi",
                    models.CharField(
                        choices=[("resep", "Resep"), ("non-resep", "Tanpa Resep")],
                        default="non-resep",
                        max_length=15,
                    ),
                ),
                (
                    "item",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="home.varianproduk",
                    ),
                ),
                (
                    "transaksi",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="home.transaksi"
                    ),
                ),
            ],
            options={
                "verbose_name": "Item",
                "verbose_name_plural": "Item",
            },
        ),
    ]
