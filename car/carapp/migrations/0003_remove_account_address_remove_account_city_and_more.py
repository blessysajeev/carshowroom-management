# Generated by Django 4.1.7 on 2023-03-07 05:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carapp', '0002_rename_is_phc_account_is_customer_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='address',
        ),
        migrations.RemoveField(
            model_name='account',
            name='city',
        ),
        migrations.RemoveField(
            model_name='account',
            name='is_customer',
        ),
        migrations.RemoveField(
            model_name='account',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='account',
            name='pincode',
        ),
        migrations.RemoveField(
            model_name='account',
            name='role',
        ),
    ]
