# Generated by Django 3.0.7 on 2020-06-05 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ThrottleApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useractivity',
            old_name='start_end',
            new_name='startend',
        ),
        migrations.RenameField(
            model_name='useractivity',
            old_name='start_time',
            new_name='starttime',
        ),
    ]
