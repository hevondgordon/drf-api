# Generated by Django 3.0.5 on 2020-04-20 04:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_post_is_liked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='is_liked',
        ),
    ]
