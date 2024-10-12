from django.contrib import admin

from .models import Bulletin, Subject, Announcement, AnnouncementDetail

admin.site.register(Bulletin)
admin.site.register(Subject)
admin.site.register(Announcement)
admin.site.register(AnnouncementDetail)
