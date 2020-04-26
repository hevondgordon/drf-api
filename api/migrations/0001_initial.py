# Generated by Django 3.0.5 on 2020-04-19 21:37
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.db import migrations

def create_standard_group():
    """ create group that standard user will belong to """
    standard_permissions = [
        'add_appointment',
        'change_appointment',
        'delete_appointment',
        'view_appointment',
        'view_business',
        'view_service',
        'view_post',
        'add_user',
        'view_user',
    ]
    standard = Group.objects.get_or_create(name='Standard')[0]
    for _permission in standard_permissions:
        permission = Permission.objects.get(
            codename=_permission,
        )
        standard.permissions.add(permission)


def create_premium_group():
    """ create group that business owner will belong to """
    premium_permissions = [
        'add_appointment',
        'change_appointment',
        'delete_appointment',
        'view_appointment',
        'add_business',
        'change_business',
        'delete_business',
        'view_business',
        'view_service',
        'add_post',
        'change_post',
        'delete_post',
        'view_post',
        'add_user',
        'view_user',
    ]
    premium = Group.objects.get_or_create(name='Premium')[0]
    for _permission in premium_permissions:
        permission = Permission.objects.get(
            codename=_permission,
        )
        premium.permissions.add(permission)


def forwards(apps, schema_editor):
    """Create groups"""
    create_standard_group()
    create_premium_group()


class Migration(migrations.Migration):

    # dependencies = [
    #      ('business', '0001_initial'),
    #      ('post', '0001_initial'),
    #      ('users', '0001_initial'),
    #      ('appointment', '0001_initial'),
    # ]

    operations = [
        #  migrations.RunPython(forwards),
    ]
