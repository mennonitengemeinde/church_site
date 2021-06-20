from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DeleteView

from church_site.views import AdminListView, BaseCreateView, BaseUpdateView, BaseDetailView
from churches.models import Church
from schedules import selectors
from shared.views import MgView
from .forms import EventForm, AttendantForm, AttendantAdminForm

from .models import Event, Attendant, EventTemplate


class EventsView(MgView):
    page_title = 'Events - Mennoniten Gemeinde'
    current_page = 'events'
    template_name = 'schedules/event-list.html'

    def get(self, request, *args, **kwargs):
        context = {
            'page_title': self.page_title,
            'current_page': self.current_page,
            'current_church': kwargs.get('church') if kwargs.get('church') else None,
            'events': selectors.get_events(church_name=kwargs.get('church')),
            'churches': Church.objects.all()
        }
        return render(request, self.template_name, context)


class EventsAdminListView(PermissionRequiredMixin, AdminListView):
    permission_required = 'schedules.view_event'
    ordering = ('-start',)
    context_object_name = 'events'
    template_name = 'schedules/events-admin-list.html'
    page_title = 'Events - Admin'
    current_page = 'manage'
    btn_add_href = reverse_lazy('schedules:events-admin-create')
    paginate_by = 25

    def get_queryset(self):
        return selectors.get_admin_events(user=self.request.user, current_events_only=True, order_by_start='asc')


class EventsAdminAllListView(EventsAdminListView):
    def get_queryset(self):
        return selectors.get_admin_events(user=self.request.user, order_by_start='asc')


class EventsAdminCreateView(PermissionRequiredMixin, BaseCreateView):
    permission_required = 'schedules.add_event'
    model = Event
    template_name = 'schedules/events-admin-form.html'
    form_class = EventForm
    success_url = reverse_lazy('schedules:events-admin-list')
    page_title = 'New Event - Admin'
    current_page = 'manage'
    btn_back_href = reverse_lazy('schedules:events-admin-list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(EventsAdminCreateView, self).get_context_data(object_list=object_list, **kwargs)
        context['event_templates'] = EventTemplate.objects.all()
        context['selected_template'] = int(self.request.GET.get('template')) if self.request.GET.get('template') else None
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_initial(self):
        if self.request.GET.get('template'):
            temp = EventTemplate.objects.get(id=self.request.GET.get('template'))
            return {
                'title': temp.title,
                'description': temp.description,
                'address': temp.address,
                'map_search_query': temp.map_search_query,
                'in_person': temp.in_person,
                'live_stream': temp.live_stream,
                'attendance_limit': temp.attendance_limit,
                'attendance_signup': temp.attendance_signup,
                'visibility': temp.visibility
            }
        else:
            return {}


class EventsAdminDetailView(PermissionRequiredMixin, BaseDetailView):
    permission_required = 'schedules.view_attendant'
    model = Event
    context_object_name = 'event'
    template_name = 'schedules/events-admin-detail.html'
    page_title = 'Event Details - Admin'
    current_page = 'manage'

    def get_queryset(self):
        return selectors.get_admin_events(user=self.request.user)


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
        return selectors.get_admin_events(user=self.request.user)

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
        return selectors.get_admin_events(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(EventsAdminDeleteView, self).delete(request, *args, **kwargs)


class EventTemplateAdminListView(PermissionRequiredMixin, AdminListView):
    permission_required = 'schedules.view_eventtemplate'
    model = EventTemplate
    context_object_name = 'event_templates'
    template_name = 'schedules/event-templates-admin-list.html'
    page_title = 'Event Templates - Admin'
    current_page = 'manage'
    btn_add_href = reverse_lazy('schedules:event-templates-admin-create')


class EventTemplateAdminCreateView(PermissionRequiredMixin, BaseCreateView):
    permission_required = 'schedules.add_eventtemplate'
    page_title = 'New Template - Admin'
    current_page = 'manage'
    btn_back_href = reverse_lazy('schedules:event-templates-admin-list')
    model = EventTemplate
    template_name = 'admin-form-view.html'
    fields = ('church', 'title', 'description', 'address', 'map_search_query', 'in_person', 'live_stream',
              'attendance_limit', 'attendance_signup', 'visibility')
    success_url = reverse_lazy('schedules:event-templates-admin-list')


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
        return selectors.get_admin_member_attendants(self.request.user)

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
        return selectors.get_admin_member_attendants(self.request.user)

    def get_context_data(self, **kwargs):
        context = super(AttendantAdminDetailView, self).get_context_data(**kwargs)
        context['btn_back_href'] = reverse_lazy('schedules:events-admin-detail',
                                                kwargs={'pk': self.kwargs.get('event')})
        return context


class AttendantAdminDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'schedules.delete_attendant'
    model = Attendant

    def get_queryset(self):
        return selectors.get_admin_member_attendants(self.request.user)

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
