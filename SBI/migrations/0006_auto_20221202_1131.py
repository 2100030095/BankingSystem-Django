# Generated by Django 3.1.8 on 2022-12-02 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SBI', '0005_auto_20221202_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeedetails',
            name='Mobile_Number',
            field=models.IntegerField(),
        ),
    ]
