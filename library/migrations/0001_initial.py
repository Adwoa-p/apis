# Generated by Django 5.1.2 on 2024-10-26 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Library',
            fields=[
                ('book_id', models.IntegerField(max_length=225, primary_key=1, serialize=False)),
                ('book_title', models.TextField(max_length=225)),
                ('book_author', models.TextField(max_length=225)),
            ],
        ),
    ]
