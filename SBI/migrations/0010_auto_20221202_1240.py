# Generated by Django 3.1.8 on 2022-12-02 07:10

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('SBI', '0009_auto_20221202_1217'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Transactions',
            new_name='Transaction',
        ),
    ]
