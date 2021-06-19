from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect
from django.views import View

from church_site.views import AdminListView, BaseDetailView

from contactus.models import ContactMessage


class AdminContactMessageListView(PermissionRequiredMixin, AdminListView):
    permission_required = 'contactus.view_contactmessage'
    template_name = 'contactus/admin-contact-messages.html'
    model = ContactMessage
    context_object_name = 'contact_messages'
    queryset = ContactMessage.objects.all_existing()
    ordering = ['-message_date']
    page_title = 'Contact Messages - Admin'
    current_page = 'manage'


class AdminContactMessageDetailView(PermissionRequiredMixin, BaseDetailView):
    permission_required = 'contactus.view_contactmessage'
    template_name = 'contactus/admin-message-detail.html'
    model = ContactMessage
    context_object_name = 'contact_msg'
    # queryset = ContactMessage.objects.all_existing
    page_title = 'Contact Message - Admin'
    current_page = 'manage'


class AdminContactMessageDeleteView(PermissionRequiredMixin, View):
    permission_required = 'contactus.delete_contactmessage'

    def post(self, request, pk=None):
        msg = ContactMessage.objects.filter(id=pk).first()
        if msg:
            msg.deleted = True
            msg.deleted_by = request.user
            msg.save()
        return redirect('contactus:admin-messages')


class AdminReadMessage(PermissionRequiredMixin, View):
    permission_required = 'contactus.change_contactmessage'

    def get(self, request, pk=None):
        msg = ContactMessage.objects.filter(id=pk).first()
        if msg:
            msg.read = not msg.read
            msg.save()
        return redirect('contactus:admin-message-detail', pk=pk)
