from datetime import datetime, timedelta, date

from django.db import models


class Bulletin(models.Model):
    title = models.CharField(max_length=150)
    year = models.IntegerField()
    week = models.IntegerField()

    class Meta:
        unique_together = ('year', 'week')
        ordering = ('year', 'week')

    def save(self, **kwargs):
        d = f'{self.year}-W{self.week}'
        first_monday = datetime.strptime(d + '-1', "%Y-W%W-%w")
        sunday_before = first_monday - timedelta(days=1)
        saturday_after = first_monday + timedelta(days=5)
        if sunday_before.month == saturday_after.month:
            self.title = f'Announcements for Week of {sunday_before.strftime("%b %d")}-{saturday_after.strftime("%d, %Y")}'
        else:
            self.title = f'Announcements for Week of {sunday_before.strftime("%b %d")}-{saturday_after.strftime("%b %d, %Y")}'
        super().save(**kwargs)

    def get_first_day_of_week(year: int, week_number: int) -> datetime:
        # Calculate the first day of the year
        first_day_of_year = datetime(year, 1, 1)
        # Calculate the first Monday of the year
        first_monday = first_day_of_year + timedelta(days=(7 - first_day_of_year.weekday()))
        # Calculate the first day of the given week
        first_day_of_week = first_monday + timedelta(weeks=week_number - 1)
        return first_day_of_week

    def __str__(self):
        return self.title


class Subject(models.Model):
    bulletin = models.ForeignKey(Bulletin, on_delete=models.CASCADE, related_name='subjects')
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title


class Announcement(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='announcements')
    time = models.CharField(max_length=50, null=True, blank=True)
    content = models.TextField()

    def __str__(self):
        return self.content[:10]


class AnnouncementDetail(models.Model):
    announcement = models.ForeignKey(Announcement, on_delete=models.CASCADE, related_name='details')
    content = models.TextField()

    def __str__(self):
        return self.content[:10]
