# Generated by Django 4.1.2 on 2022-10-23 17:03

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dental', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('medical_card', '0002_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MedicalCarts',
            new_name='MedicalCards',
        ),
    ]
