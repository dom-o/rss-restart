# Generated by Django 3.2.1 on 2021-05-06 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rss', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rssfeed',
            name='url',
            field=models.URLField(default='https://awardsforgoodboys.substack.com/feed'),
            preserve_default=False,
        ),
    ]
