# Generated by Django 5.0.4 on 2024-04-17 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_appointment_userprofile_chat_log_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='appointments',
            field=models.ManyToManyField(to='main.appointment'),
        ),
    ]
