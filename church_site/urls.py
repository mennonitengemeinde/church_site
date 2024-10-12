from allauth.account.views import confirm_email, email_verification_sent
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework import routers

# from telegram.api.controllers import LiveSubscriptionViewSet

router = routers.DefaultRouter()
# router.register(r'subscription/live', LiveSubscriptionViewSet)
# router.register(r'streams', StreamsViewSet)

urlpatterns = [
    path("", include("core.urls")),
    path(settings.ADMIN_URL, admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("api/v1/", include(router.urls)),
    path("api/v1/streams/", include("streams.api.urls")),
    # path('api/v1/telegram/', include('telegram.api_urls')),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path(
        "dj-rest-auth/registration/account-confirm-email/<str:key>/",
        confirm_email,
        name="account_email_verification_sent",
    ),
    path(
        "dj-rest-auth/registration/account-email-verification-sent/",
        email_verification_sent,
        name="account_email_verification_sent",
    ),
    path("dj-rest-auth/", include("dj_rest_auth.urls")),
    path("dj-rest-auth/registration/", include("dj_rest_auth.registration.urls")),
    path("users/", include("accounts.urls")),
    path("bulletin/", include("bulletin.urls")),
    path("churches/", include("churches.urls")),
    path("speakers/", include("speakers.urls")),
    path("schedules/", include("schedules.urls")),
    path("sermons/", include("sermons.urls")),
    path("streams/", include("streams.urls")),
    path("contactus/", include("contactus.urls")),
    path("forms/", include("forms.urls")),
    path("robots.txt", TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    path("sitemap.xml", TemplateView.as_view(template_name="sitemap.xml", content_type="text/xml")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
