# Generated by Django 4.2.1 on 2023-05-11 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ContactManager', '0003_contact_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='map_link',
        ),
    ]
