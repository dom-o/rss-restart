# Generated by Django 3.2.1 on 2021-06-19 00:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rss', '0004_auto_20210618_1955'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rssitem',
            old_name='link',
            new_name='content_link',
        ),
    ]
