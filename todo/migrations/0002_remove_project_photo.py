# Generated by Django 4.0.4 on 2022-07-28 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='photo',
        ),
    ]
