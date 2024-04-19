from django.apps import apps
from django.contrib import admin

from home.models import Pembelian, PembelianObat

# Register your models here.


class PembelianObatInline(admin.TabularInline):
    model = PembelianObat
    extra = 1
    exclude = ("uid",)


@admin.register(Pembelian)
class PembelianAdmin(admin.ModelAdmin):
    search_fields = [
        "nomor_pre_order",
        "nomor_faktur",
        "supplier",
    ]
    inlines = [PembelianObatInline]


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
            if model.__name__ not in ["Pembelian", "PembelianObat"]:
                admin.site.register(model)

    except Exception:
        pass
