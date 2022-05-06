from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Task(models.Model):
    # Creating choices for char field
    OPENING = 'Opening'
    IN_PROGRESS = 'In progress'
    OVERDUE = 'Overdue'
    DONE = 'Done'
    STATUS = [
        (OPENING, 'Opening'),
        (IN_PROGRESS, 'In progress'),
        (OVERDUE, 'Overdue'),
        (DONE, 'Done')
    ]

    id = models.AutoField(primary_key=True)  # task id
    name = models.CharField(max_length=100)  # task name
    description = models.TextField(max_length=255)  # task decription
    category = models.ForeignKey('TaskCategory', on_delete=models.PROTECT, null=True)  # task category
    priority = models.PositiveIntegerField(default=1, validators=[MinValueValidator(0), MaxValueValidator(100)])  #
    # task priority
    status = models.CharField(max_length=32, choices=STATUS, default=OPENING)  # task status
    deadline = models.DateTimeField(null=True)  # task deadline
    time_create = models.DateTimeField(auto_now_add=True)  # task time created
    time_update = models.DateTimeField(auto_now=True)  # task time updated
    author = models.ForeignKey('auth.User', related_name='task', on_delete=models.CASCADE, null=True)  # task's author

    def __str__(self):
        """

        This function allows to work with instance

        """

        return self.name


class TaskCategory(models.Model):
    id = models.AutoField(primary_key=True)  # category id
    name = models.CharField(max_length=100)  # category name

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        """

        This function allows to work with instance

        """
        return self.name
