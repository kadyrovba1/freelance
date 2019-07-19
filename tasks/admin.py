
from django.contrib import admin
from .models import Task

# Register your models here.

admin.site.register(Task)

class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'owner', 'title', 'description', 'price']