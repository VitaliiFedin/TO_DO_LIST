from django.db import models


# Create your models here.
class Task(models.Model):
    OPENING = 'Opening'
    INPROGRESS = 'In progress'
    OVERDUE = 'Overdue'
    STATUS = [
        (OPENING, 'Task is opening'),
        (INPROGRESS, 'Task in progress'),
        (OVERDUE, 'Task is overdue')
    ]
    task_id = models.AutoField(primary_key=True)
    task_name = models.CharField(max_length=100)
    task_description = models.TextField(max_length=255)
    category = models.ForeignKey('TaskCategory', on_delete=models.PROTECT)
    status = models.CharField(max_length=32, choices=STATUS, default=OPENING)
    deadline = models.DateTimeField()
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task_name


class TaskCategory(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "categories"
    def __str__(self):
        return self.category_name