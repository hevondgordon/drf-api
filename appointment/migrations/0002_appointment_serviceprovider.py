# Generated by Django 3.0 on 2020-03-28 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0001_initial'),
        ('appointment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='serviceProvider',
            field=models.ManyToManyField(related_name='appointments', to='business.Business'),
        ),
    ]
