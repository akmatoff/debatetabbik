from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView

urlpatterns = (
    [
        path("admin/", admin.site.urls),
        re_path(r"^auth/", include("drf_social_oauth2.urls", namespace="drf")),
        path(
            "api/",
            include(
                [
                    path("schema/", SpectacularAPIView.as_view(), name="schema"),
                    path(
                        "schema/swagger-ui/",
                        SpectacularSwaggerView.as_view(),
                        name="swagger-ui",
                    ),
                    path("users/", include("users.urls", namespace="users")),
                    path(
                        "clubs/",
                        include("clubs.urls", namespace="clubs"),
                    ),
                    path(
                        "tournaments/",
                        include("tournaments.urls", namespace="tournaments"),
                    ),
                ],
            ),
        ),
        path("api-auth/", include("rest_framework.urls")),
    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
