from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import View

from church_site.views import BaseListView, AdminListView, BaseCreateView, BaseUpdateView, BaseDetailView
from churches.models import Church
from .forms import EventForm, AttendantForm

from .models import Event, Attendant


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


class AttendantCreateView(SuccessMessageMixin, BaseCreateView):
    model = Attendant
    template_name = 'schedules/attendant-create-form.html'
    form_class = AttendantForm
    success_url = reverse_lazy('home:home')
    page_title = 'Signup attendance'
    current_page = 'events'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(AttendantCreateView, self).get_context_data(**kwargs)
        context['event'] = Event.objects.get(id=self.kwargs.get('event'))
        return context

    def get_initial(self):
        initial = super(AttendantCreateView, self).get_initial()
        initial['event'] = self.kwargs.get('event')
        return initial

    def get_success_message(self, cleaned_data):
        if cleaned_data.get('amount') > 1:
            people = 'people'
        else:
            people = 'person'
        return f"{cleaned_data.get('full_name')}, you have successfully signup {cleaned_data.get('amount')} {people} " \
               f"to attend {cleaned_data.get('event').title} at {cleaned_data.get('event').church}"


class AttendantAdminDetailView(PermissionRequiredMixin, BaseDetailView):
    permission_required = 'schedules.view_attendant'
    model = Event
    context_object_name = 'event'
    template_name = 'schedules/attendant-admin-detail.html'
    page_title = 'Attendant Details - Admin'
    current_page = 'manage'

    def get_object(self, queryset=None):
        event = super(AttendantAdminDetailView, self).get_object(queryset)
        return event

    def get_queryset(self):
        # queryset.filter(attendance_limit__gt=0, start__gte=timezone.now(), church__members=self.request.user)
        return Event.objects.filter(church__members=self.request.user)
        # return queryset


class AttendantAdminSignupToggle(PermissionRequiredMixin, View):
    permission_required = 'schedules.change_attendant'

    # This will change the signup status
    def get(self, request, pk=None):
        event = Event.objects.filter(id=pk).first()
        if event:
            event.attendance_signup = not event.attendance_signup
            event.save()
        return redirect('schedules:events-admin-list')
