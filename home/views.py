from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def index(request):

    # Page from the theme
    return render(request, "pages/index.html")


@login_required(login_url="/accounts/login/")
def pos_page(request):
    context = {
        "segment": "pos_page",
    }
    return render(request, "pages/pos.html", context)
