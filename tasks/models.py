from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=1, null=True)
    created_time = models.DateTimeField(auto_now_add=True)
    executor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='executor')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default='', related_name='task')
    ready = models.BooleanField(default=False)
    accept = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'task'
        verbose_name_plural = 'tasks'

    def __str__(self):
        return self.title

