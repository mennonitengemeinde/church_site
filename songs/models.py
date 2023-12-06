from django.db import models


class Choir(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='choirs', null=True, blank=True)

    church = models.ForeignKey('churches.Church', on_delete=models.PROTECT, related_name='choirs')

    class Meta:
        ordering = ('name',)
        unique_together = ('name', 'church')

    def __str__(self):
        return self.name


class Song(models.Model):
    title = models.CharField(max_length=255)
    video_url = models.URLField(null=True, blank=True)

    choir = models.ForeignKey(Choir, on_delete=models.PROTECT, related_name='songs')
    event = models.ForeignKey('schedules.Event', on_delete=models.PROTECT, related_name='songs')

    def __str__(self):
        return self.title
