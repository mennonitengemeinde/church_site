"""church_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from allauth.account.views import confirm_email

from streams.api.controllers import StreamsViewSet
from telegram.api.controllers import LiveSubscriptionViewSet

router = routers.DefaultRouter()
router.register(r'subscription/live', LiveSubscriptionViewSet)
router.register(r'streams', StreamsViewSet)

urlpatterns = [
    path('', include('home.urls')),
    url('', include('pwa.urls')),
    path(settings.ADMIN_URL, admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
    path('api/v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
    url(r"^rest-auth/registration/account-confirm-email/(?P<key>[\s\d\w().+-_',:&]+)/$", confirm_email,
        name="account_confirm_email"),
    path('users/', include('accounts.urls')),
    path('churches/', include('churches.urls')),
    path('speakers/', include('speakers.urls')),
    path('schedules/', include('schedules.urls')),
    path('sermons/', include('sermons.urls')),
    path('streams/', include('streams.urls')),
    path('contactus/', include('contactus.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
