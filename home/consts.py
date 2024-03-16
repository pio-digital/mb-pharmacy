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
