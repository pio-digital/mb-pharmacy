from collections import namedtuple

from django.utils.translation import gettext_lazy as _

Currency = namedtuple("currency", ["base", "iso_code", "symbol", "name"])

CURRENCY_EUR = "eur"
CURRENCY_JPY = "jpy"
CURRENCY_USD = "usd"
CURRENCY_SGD = "sgd"
CURRENCY_IDR = "idr"

CURRENCIES = {
    CURRENCY_EUR: Currency(base=100, iso_code="eur", symbol="€", name=_("Euro")),
    CURRENCY_USD: Currency(base=100, iso_code="usd", symbol="$", name=_("US Dollar")),
    CURRENCY_SGD: Currency(
        base=100, iso_code="sgd", symbol="S$", name=_("Singapore Dollar")
    ),
    CURRENCY_IDR: Currency(
        base=1, iso_code="idr", symbol="Rp", name=_("Indonesian Rupiah")
    ),
    CURRENCY_JPY: Currency(base=1, iso_code="jpy", symbol="¥", name=_("Japanese Yen")),
}

CURRENCY_LIST = [CURRENCY_JPY, CURRENCY_IDR, CURRENCY_SGD, CURRENCY_EUR, CURRENCY_USD]
CURRENCY_CHOICES = [(c, c) for c in CURRENCY_LIST]

SUCCESS = "success"
PENDING = "pending"
CANCELLED = "cancelled"
VOID = "void"
STATUS_CHOICES = (
    (SUCCESS, _("Sukses")),
    (PENDING, _("Tertunda")),
    (CANCELLED, _("Dibatalkan")),
    (VOID, _("Void")),
)

ADMIN = "admin"
CASHIER = "cashier"
ROLE_CHOICES = (
    (ADMIN, _("Admin")),
    (CASHIER, _("Kasir")),
)

PRESCRIPTION = "resep"
NON_PRESCRIPTION = "non-resep"
TRANSACTION_TYPE_CHOICES = (
    (PRESCRIPTION, _("Resep")),
    (NON_PRESCRIPTION, _("Tanpa Resep")),
)


CALCULATION_FIELDS = [
    "total",
    "pajak",
    "nominal_pajak",
    "diskon",
    "nominal_diskon",
    "persentase_margin",
    "nominal_margin",
]


METODE_PEMBAYARAN_TUNAI_ID = 1
METODE_PEMBAYARAN_BANK_TRANSFER_ID = 2

UNIT_BOX = "Box"  # Level 1
UNIT_STRIP = "Strip"  # Level 2
UNIT_PCS = "Pcs"  # Level 3
