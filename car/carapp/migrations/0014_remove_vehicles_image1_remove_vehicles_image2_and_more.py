# Generated by Django 4.1.7 on 2023-03-16 08:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carapp', '0013_staff_remove_food_registration_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicles',
            name='image1',
        ),
        migrations.RemoveField(
            model_name='vehicles',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='vehicles',
            name='image3',
        ),
        migrations.RemoveField(
            model_name='vehicles',
            name='image4',
        ),
        migrations.RemoveField(
            model_name='vehicles',
            name='image5',
        ),
        migrations.RemoveField(
            model_name='vehicles',
            name='image6',
        ),
        migrations.AddField(
            model_name='vehicles',
            name='images',
            field=models.ImageField(choices=[('image1', 'image 1'), ('image2', 'image 2'), ('image3', 'image 3'), ('image4', 'image 4'), ('image5', 'image 5'), ('image6', 'image 6')], default=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='vehicles',
            name='name',
            field=models.CharField(max_length=250, unique=True, validators=[django.core.validators.RegexValidator('^[A-Z ]*$', 'Only uppercase letters\xa0\xa0allowed.')]),
        ),
    ]