from django.contrib import admin
from django.urls import include, path

try:
    from rest_framework.authtoken.views import obtain_auth_token
except Exception:
    pass

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("admin_datta.urls")),
    path("", include("home.urls")),
    path("login/jwt/", view=obtain_auth_token),
]


# Lazy-load on routing is needed
# During the first build, API is not yet generated
try:
    urlpatterns.append(path("api/", include("api.urls")))
    urlpatterns.append(path("login/jwt/", view=obtain_auth_token))
except Exception:
    pass
