from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class EmployeeDetails(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    Mobile_Number = models.IntegerField()
    Name = models.CharField(max_length=100,null=True)
    Email = models.CharField(max_length=100,null=True)
    Account = models.CharField(max_length=15,null=True)
    gender = models.CharField(max_length=50,null=True)



    def _str_(self):
        return self.user.username

class Transactions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    balance=models.IntegerField()
    def _str_(self):
        return self.balance


class Loans(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Name=models.CharField(max_length=50)
    Mobile=models.IntegerField()
    Email=models.CharField(max_length=100)
    Proof=models.CharField(max_length=50)


    def _str_(self):
        return self.Proof


class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Name=models.CharField(max_length=50)
    Account_balance=models.IntegerField()

    def _str_(self):
        return self.Account_balance

class Docc(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    File=models.FileField()

    def _str_(self):
        return self.File







# Create your models here.
