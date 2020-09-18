# Generated by Django 2.2.15 on 2020-09-16 15:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0015_remove_video_search'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='user',
        ),
        migrations.AddField(
            model_name='tag',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]