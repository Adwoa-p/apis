# Generated by Django 5.1.2 on 2025-02-13 03:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='visibilty',
            new_name='visibility',
        ),
    ]
