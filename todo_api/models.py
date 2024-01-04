from django.db import models

# Create your models here.


class TodoStatus(models.Model):
    status_name = models.CharField(max_length=50)

    def __str__(self):
        return self.status_name


class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    status = models.ForeignKey(TodoStatus, on_delete=models.CASCADE)
    task_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


