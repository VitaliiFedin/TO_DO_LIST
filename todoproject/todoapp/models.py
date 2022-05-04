from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


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
    category = models.ForeignKey('TaskCategory', on_delete=models.PROTECT, null=True)
    task_priority = models.PositiveIntegerField(default=1, validators=[MinValueValidator(0), MaxValueValidator(100)])
    status = models.CharField(max_length=32, choices=STATUS, default=OPENING)
    deadline = models.DateTimeField(null=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey('auth.User', related_name='task', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.task_name


class TaskCategory(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.category_name
