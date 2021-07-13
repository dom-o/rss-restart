# Generated by Django 3.2.1 on 2021-07-02 19:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rss', '0007_rssfeed_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rssitem',
            name='content_link',
            field=models.TextField(validators=[django.core.validators.URLValidator()]),
        ),
    ]
