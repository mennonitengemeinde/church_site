# Generated by Django 3.2.4 on 2021-06-20 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0003_auto_20200613_2037'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('map_search_query', models.CharField(blank=True, max_length=300, null=True)),
                ('in_person', models.BooleanField(default=True)),
                ('live_stream', models.BooleanField(default=False)),
                ('attendance_limit', models.IntegerField(default=0)),
                ('attendance_signup', models.BooleanField(default=False)),
                ('visibility', models.CharField(choices=[('public', 'Public'), ('private', 'Private'), ('members', 'Members Only')], max_length=50)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]
