from django.db import models
from users.models import User
# Create your models here.


class Task(models.Model):
    owner = models.ForeignKey(User, related_name='tasks', on_delete=models.CASCADE)
    title = models.CharField(max_length=55)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_time = models.DateTimeField(auto_now_add=True)
    executor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='executor')

    class Meta:
        ordering = ['-created_time']

    def __str__(self):
        return '{}-{}'.format(self.title, self.price)
