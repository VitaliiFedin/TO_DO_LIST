# Generated by Django 3.2.13 on 2022-05-04 10:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0018_alter_task_task_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_priority',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]