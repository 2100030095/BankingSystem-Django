# Generated by Django 4.1.3 on 2022-12-03 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SBI', '0016_loans_loan_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loans',
            name='Loan_type',
        ),
    ]
