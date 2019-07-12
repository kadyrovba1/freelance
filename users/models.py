from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    CUSTOMER = 1
    EXECUTOR = 2

    USER_TYPES = (
        (CUSTOMER, (u"Заказчик")),
        (EXECUTOR, (u"Исполнитель")),
    )

    # First Name and Last Name do not cover name patterns
    # around the globe.
    email = models.EmailField(verbose_name='email', unique='True')
    name = models.CharField(('Name of User'), blank=True, max_length=255)
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPES, default=EXECUTOR)
    balance = models.DecimalField(decimal_places=2, max_digits=7, default=0)

    def __str__(self):
        return self.username