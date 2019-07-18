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

    def update_balance(self, balance, reason, user):
        with transaction.atomic():
            if reason is Transaction.REPLENISH:
                User.objects.select_for_update().filter(id=user.id).filter(id=user.id).update(balance=user.balance+balance)
            elif reason is Transaction.WITHDRAWAL:
                User.objects.select_for_update().filter(id=user.id).update(balance=user.balance-balance)


class Transaction(models.Model):
    REPLENISH = 1
    WITHDRAWAL = 2

    CHOICES = (
        (REPLENISH, 'Пополнить'),
        (WITHDRAWAL, 'Вывод'),
    )

    user = models.ForeignKey(
        'User', related_name='balance_changes',
        on_delete=models.CASCADE
    )

    action = models.PositiveSmallIntegerField(choices=CHOICES, default=REPLENISH)
    amount = models.DecimalField('Amount', default=0, max_digits=18, decimal_places=6)
    created_time = models.DateTimeField(auto_now_add=True)