# Generated by Django 3.0.7 on 2020-06-05 12:33

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('ids', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('real_name', models.CharField(max_length=30)),
                ('tz', models.CharField(default='Asia/Kolkata', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='UserActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('start_end', models.DateTimeField(default=django.utils.timezone.now)),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity_periods', to='ThrottleApp.User')),
            ],
        ),
    ]
