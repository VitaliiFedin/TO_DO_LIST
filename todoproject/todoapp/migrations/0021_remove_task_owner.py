# Generated by Django 3.2.13 on 2022-05-04 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0020_task_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='owner',
        ),
    ]
