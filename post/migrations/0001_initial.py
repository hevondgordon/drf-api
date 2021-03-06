# Generated by Django 3.0 on 2020-03-28 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('business', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=200)),
                ('like_count', models.IntegerField()),
                ('is_liked', models.BooleanField(default=False)),
                ('category', models.CharField(max_length=100)),
                ('media_url', models.CharField(max_length=100)),
                ('media_type', models.CharField(max_length=50)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.Business')),
            ],
        ),
    ]
