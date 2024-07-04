# Generated by Django 4.2.8 on 2024-06-30 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_alter_pembayaran_options_alter_pembelian_options"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="produk",
            name="kemasan",
        ),
        migrations.AddField(
            model_name="metodepembayaran",
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
            name="tanggal_jatuh_tempo",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="produk",
            name="pieces_per_kemasan",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="produk",
            name="unit",
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, to="home.unit"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="sumberdana",
            name="saldo",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="varianproduk",
            name="kuantitas",
            field=models.FloatField(default=0),
        ),
    ]
