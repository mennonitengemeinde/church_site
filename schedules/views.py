from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.utils import timezone

from church_site.views import BaseListView, AdminListView, BaseCreateView, BaseUpdateView
from churches.models import Church
from .forms import EventForm

from .models import Event


class EventsListView(BaseListView):
    page_title = 'Events - Mennoniten Gemeinde'
    current_page = 'events'
    model = Event
    template_name = 'schedules/event-list.html'
    context_object_name = 'events'

    def get_queryset(self):
        if self.kwargs.get('church'):
            return self.model.objects.filter(end__gt=timezone.now(), church__name=self.kwargs.get('church').replace('-', ' '))
        return self.model.objects.filter(end__gt=timezone.now())

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_church'] = self.kwargs.get('church') if self.kwargs.get('church') else None
        context['churches'] = Church.objects.all()
        return context


class EventsAdminListView(PermissionRequiredMixin, AdminListView):
    permission_required = 'schedules.view_event'
    model = Event
    ordering = ('-start',)
    context_object_name = 'events'
    template_name = 'schedules/events-admin-list.html'
    page_title = 'Events - Admin'
    current_page = 'manage'
    btn_add_href = reverse_lazy('schedules:events-admin-create')
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.member_events(user=self.request.user)
        return queryset


class EventsAdminCreateView(PermissionRequiredMixin, BaseCreateView):
    permission_required = 'schedules.add_event'
    model = Event
    template_name = 'schedules/events-admin-form.html'
    form_class = EventForm
    success_url = reverse_lazy('schedules:events-admin-list')
    page_title = 'New Event - Admin'
    current_page = 'manage'
    btn_back_href = reverse_lazy('schedules:events-admin-list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class EventsAdminUpdateView(PermissionRequiredMixin, BaseUpdateView):
    permission_required = 'schedules.change_event'
    model = Event
    template_name = 'schedules/events-admin-form.html'
    form_class = EventForm
    success_url = reverse_lazy('schedules:events-admin-list')
    page_title = 'Update Event - Admin'
    current_page = 'manage'
    btn_back_href = reverse_lazy('schedules:events-admin-list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

