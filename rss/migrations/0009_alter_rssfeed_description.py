# Generated by Django 3.2.1 on 2021-07-08 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rss', '0008_alter_rssitem_content_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rssfeed',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
    ]
