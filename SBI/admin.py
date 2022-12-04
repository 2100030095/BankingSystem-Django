from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import *


@admin.register(EmployeeDetails)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in
                    EmployeeDetails._meta.get_fields()]

@admin.register(Transactions)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in
                    Transactions._meta.get_fields()]

@admin.register(Loans)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in
                    Loans._meta.get_fields()]


@admin.register(Docc)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in
                    Docc._meta.get_fields()]

@admin.register(Account)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in
                    Account._meta.get_fields()]


