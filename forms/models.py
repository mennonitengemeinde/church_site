from django.db import models

LANGUAGES = (
    ('en', 'English'),
    ('es', 'Spanish'),
    ('de', 'German'),
)


class Form(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255)
    description = models.TextField(blank=True)
    language = models.CharField(max_length=2, choices=LANGUAGES, default='en')
    embed_url = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Translation(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    language = models.CharField(max_length=2, choices=LANGUAGES, default='en')
    embed_url = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        unique_together = ('form', 'language')
