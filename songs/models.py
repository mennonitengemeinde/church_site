from django.db import models


class Song(models.Model):
    title = models.CharField(max_length=255)
    video_url = models.URLField(null=True, blank=True)

    choir = models.ForeignKey('churches.Choir', on_delete=models.PROTECT, related_name='songs')
    event = models.ForeignKey('schedules.Event', on_delete=models.PROTECT, related_name='songs')

    def __str__(self):
        return self.title
