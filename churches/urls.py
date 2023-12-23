from django.urls import path

from .views import (
    ChurchesAdminListView,
    ChurchesAdminCreateView,
    ChurchesAdminUpdateView,
    AdminChoirCreateView,
    ChurchesAdminDetailView,
)

app_name = "churches"

urlpatterns = [
    path(
        "manage/churches/", ChurchesAdminListView.as_view(), name="churches-admin-list"
    ),
    path(
        "manage/churches/<int:pk>/",
        ChurchesAdminDetailView.as_view(),
        name="churches-admin-detail",
    ),
    path(
        "manage/churches/add/",
        ChurchesAdminCreateView.as_view(),
        name="churches-admin-create",
    ),
    path(
        "manage/churches/<int:pk>/update/",
        ChurchesAdminUpdateView.as_view(),
        name="churches-admin-update",
    ),
    path(
        "manage/churches/<int:pk>/choirs/create/",
        AdminChoirCreateView.as_view(),
        name="manage_choirs_create",
    ),
]
