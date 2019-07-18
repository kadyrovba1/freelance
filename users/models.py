from django.db import models, transaction
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
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPES, default=EXECUTOR)
    balance = models.DecimalField(decimal_places=2, max_digits=7, default=0)

    def __str__(self):
        return self.email
