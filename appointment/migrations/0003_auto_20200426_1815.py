# Generated by Django 3.0.5 on 2020-04-26 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0002_auto_20200426_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='comment',
            field=models.CharField(max_length=100, null=True),
        ),
    ]