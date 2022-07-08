from django.urls import path

from .views import (FormsDetailView, AdminFormListView, AdminFormCreateView, AdminTranslationListView,
                    AdminTranslationCreateView, AdminFormUpdateView, AdminTranslationUpdateView)

app_name = 'forms'

urlpatterns = [
    path('<str:slug>/', FormsDetailView.as_view(), name='forms-detail'),
    path('manage/forms/', AdminFormListView.as_view(), name='admin-forms-list'),
    path('manage/forms/create/', AdminFormCreateView.as_view(), name='admin-forms-create'),
    path('manage/forms/<str:slug>/', AdminTranslationListView.as_view(), name='admin-forms-detail'),
    path('manage/forms/<str:slug>/update/', AdminFormUpdateView.as_view(), name='admin-forms-update'),
    path('manage/forms/<str:slug>/translations/create/', AdminTranslationCreateView.as_view(),
         name='admin-translation-create'),
    path('manage/forms/<str:slug>/translations/<int:pk>/update/', AdminTranslationUpdateView.as_view(),
         name='admin-translation-update'),
    # path('manage/messages/<int:pk>/read/', AdminReadMessage.as_view(), name='admin-read-message'),
    # path('manage/messages/<int:pk>/delete/', AdminContactMessageDeleteView.as_view(), name='admin-delete-message'),
]
