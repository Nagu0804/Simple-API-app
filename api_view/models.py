from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group, Permission
from django.utils.translation import gettext as _


class UserTable(AbstractUser):
    email = models.EmailField(unique=True)

    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        related_name='custom_user_set'  
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='custom_user_set' 
    )

    def __str__(self):
        return self.username

class EmployeeTable(models.Model):
    empId = models.AutoField(primary_key=True)
    empName = models.CharField(max_length=100)
    empDateofJoin = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.empName

class AttendanceTable(models.Model):
    empId = models.ForeignKey(EmployeeTable, on_delete=models.CASCADE)
    Date = models.DateField()
    Attendance = models.BooleanField()
    WorkingHour = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return f"Attendance for {self.empId} on {self.Date}"