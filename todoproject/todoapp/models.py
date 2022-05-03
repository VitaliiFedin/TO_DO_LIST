from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.
from rest_framework import request
from django.contrib.auth.models import User

class Task(models.Model):
    OPENING = 'Opening'
    INPROGRESS = 'In progress'
    OVERDUE = 'Overdue'
    DONE = 'Done'
    STATUS = [
        (OPENING, 'Opening'),
        (INPROGRESS, 'In progress'),
        (OVERDUE, 'Overdue'),
        (DONE, 'Done')
    ]
    task_id = models.AutoField(primary_key=True)
    task_name = models.CharField(max_length=100)
    task_description = models.TextField(max_length=255)
    category = models.ForeignKey('TaskCategory', on_delete=models.PROTECT,null=True)
    task_priority = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(100)])
    status = models.CharField(max_length=32, choices=STATUS, default=OPENING)
    deadline = models.DateTimeField(null=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE,null=True)
    #author = models.CharField(max_length=122,default=current_user)




    def __str__(self):
        return self.task_name


class TaskCategory(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.category_name
