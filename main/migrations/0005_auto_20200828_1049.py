# Generated by Django 2.2.15 on 2020-08-28 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200828_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='tags',
            field=models.ManyToManyField(blank=True, to='main.Tag'),
        ),
    ]
