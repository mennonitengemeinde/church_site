from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import View
from django.views.generic import DeleteView

from church_site.views import BaseListView, AdminListView, BaseCreateView, BaseUpdateView, BaseDetailView
from churches.models import Church
from schedules import selectors
from .forms import EventForm, AttendantForm, AttendantAdminForm

from .models import Event, Attendant


class EventsView(View):
    page_title = 'Events - Mennoniten Gemeinde'
    current_page = 'events'
    template_name = 'schedules/event-list.html'

    def get(self, request, *args, **kwargs):
        context = {
            'current_church': kwargs.get('church') if kwargs.get('church') else None,
            'events': selectors.get_event_list(kwargs.get('church'))
        }
        return render(request, self.template_name, context)


# class EventsListView(BaseListView):
#     page_title = 'Events - Mennoniten Gemeinde'
#     current_page = 'events'
#     model = Event
#     template_name = 'schedules/event-list.html'
#     context_object_name = 'events'
#
#     def get_queryset(self):
#         if self.kwargs.get('church'):
#             return self.model.objects.filter(end__gt=timezone.now(), church__name=self.kwargs.get('church').replace('-', ' '))
#         return self.model.objects.filter(end__gt=timezone.now())
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['current_church'] = self.kwargs.get('church') if self.kwargs.get('church') else None
#         context['churches'] = Church.objects.all()
#         return context


class EventsAdminListView(PermissionRequiredMixin, AdminListView):
    permission_required = 'schedules.view_event'
    model = Event
    ordering = ('-start',)
    context_object_name = 'events'
    template_name = 'schedules/events-admin-list.html'
    page_title = 'Events - Admin'
    current_page = 'manage'
    btn_add_href = reverse_lazy('schedules:events-admin-create')
    paginate_by = 25
    
    def get_queryset(self):
        return self.model.objects.current_memeber_only_events(user=self.request.user)


class EventsAdminAllListView(EventsAdminListView):
    def get_queryset(self):
        return self.model.objects.member_only_events(self.request.user)


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


class EventsAdminDetailView(PermissionRequiredMixin, BaseDetailView):
    permission_required = 'schedules.view_attendant'
    model = Event
    context_object_name = 'event'
    template_name = 'schedules/events-admin-detail.html'
    page_title = 'Event Details - Admin'
    current_page = 'manage'

    def get_queryset(self):
        return self.model.objects.member_only_events(self.request.user)


class EventsAdminUpdateView(PermissionRequiredMixin, BaseUpdateView):
    permission_required = 'schedules.change_event'
    model = Event
    template_name = 'schedules/events-admin-form.html'
    form_class = EventForm
    success_url = reverse_lazy('schedules:events-admin-list')
    page_title = 'Update Event - Admin'
    current_page = 'manage'
    btn_back_href = reverse_lazy('schedules:events-admin-list')

    def get_queryset(self):
        return self.model.objects.member_only_events(self.request.user)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class EventsAdminDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'schedules.delete_event'
    model = Event
    success_url = reverse_lazy('schedules:events-admin-list')
    success_message = 'Event was deleted successfully'

    def get_queryset(self):
        return self.model.objects.member_only_events(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(EventsAdminDeleteView, self).delete(request, *args, **kwargs)


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


class AttendantAdminUpdateView(PermissionRequiredMixin, BaseUpdateView):
    permission_required = 'schedules.change_attendant'
    template_name = 'admin-form-view.html'
    model = Attendant
    context_object_name = 'attendant'
    form_class = AttendantAdminForm
    page_title = 'Update Attendant - Admin'

    def get_queryset(self):
        return self.model.objects.get_member_attendants(self.request.user)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(AttendantAdminUpdateView, self).get_context_data(**kwargs)
        context['btn_back_href'] = reverse_lazy('schedules:attendants-admin-detail', kwargs={
            'event': self.kwargs.get('event'), 'pk': self.kwargs.get('pk')})
        return context

    def get_success_url(self):
        return reverse_lazy('schedules:attendants-admin-detail', kwargs={'event': self.kwargs.get('event'),
                                                                         'pk': self.kwargs.get('pk')})


class AttendantAdminDetailView(PermissionRequiredMixin, BaseDetailView):
    permission_required = 'schedules.view_attendant'
    template_name = 'schedules/attendant-admin-detail.html'
    model = Attendant
    context_object_name = 'attendant'
    page_title = 'Attendant Detail - Admin'

    def get_queryset(self):
        return self.model.objects.get_member_attendants(self.request.user)

    def get_context_data(self, **kwargs):
        context = super(AttendantAdminDetailView, self).get_context_data(**kwargs)
        context['btn_back_href'] = reverse_lazy('schedules:events-admin-detail',
                                                kwargs={'pk': self.kwargs.get('event')})
        return context


class AttendantAdminDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'schedules.delete_attendant'
    model = Attendant

    def get_queryset(self):
        return self.model.objects.get_member_attendants(self.request.user)

    def get_success_url(self):
        return reverse_lazy('schedules:events-admin-detail', kwargs={'pk': self.kwargs.get('event')})


class AttendantAdminSignupToggle(PermissionRequiredMixin, View):
    permission_required = 'schedules.change_attendant'

    # This will change the signup status
    def get(self, request, pk=None):
        event = Event.objects.filter(id=pk).first()
        if event:
            event.attendance_signup = not event.attendance_signup
            event.save()
        return redirect('schedules:events-admin-list')
