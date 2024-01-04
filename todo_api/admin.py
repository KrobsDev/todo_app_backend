from django.contrib import admin
from .models import TodoStatus, Todo

# Register your models here.
admin.site.register(Todo)
admin.site.register(TodoStatus)