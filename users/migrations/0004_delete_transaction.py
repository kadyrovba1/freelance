# Generated by Django 2.2.3 on 2019-07-19 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_transaction'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Transaction',
        ),
    ]
