# Generated by Django 3.0 on 2020-03-29 00:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0001_initial'),
        ('appointment', '0003_auto_20200328_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='service_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.Service'),
        ),
    ]
