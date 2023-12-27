from django.db import models
from datetime import date
from category.models import category
# Create your models here.
class Task(models.Model):
    taskTitle = models.CharField(max_length=50)
    taskDescription = models.TextField()
    is_completed = models.BooleanField(default=False)
    TaskAssignDate = models.DateField(default=date.today) 
    taskCategories = models.ManyToManyField(category)


    def __str__(self):
        return self.taskTitle