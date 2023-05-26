from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Tasks for Personnel API
# Develop Models for Personnel and Department and create relations
# Develop Serializers
# Create Views
# Add permission to your views.
# Specifically for PersonnelView. Only privileged staff can do POST, PUT and DELETE operations.
# Others can only do GET operations
# Automatically add the current user as added_by field while creating a new personnel
# Create Urls
# Create Account_app and handle authorization

# Bonus Tasks:
# In DepartmentView in addition to department names also display the personnel in that department too
# Add serializer methodfield to display personnel count in that deparment
# Add serializer methodfield to display how many days passed since that personnel registered to that company
# While creating a new personnel, if a personnel's is_staff = True then also Create a record in the User table
# Add a validation for salary. Don't let negative numbers to be a salary
# Create a different DepartmentSerializer for staff personnel and use that serializer for only staff







class Personnel(models.Model):
    # m = 'Male'
    # f = 'Female'
    # o = 'Other'
    
    OPTIONS = [
        ('m', "Male"),
        ('f', "Female"),
        ('o', "Other"),
    ]
    
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)    
    salary = models.IntegerField()
    email = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=OPTIONS, null=True, blank=True)
    date_joined = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=30)
    is_staff = models.BooleanField()
    added_by = models.ForeignKey(User, on_delete=models.PROTECT)
    department = models.ForeignKey('Department', on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Department(models.Model):
    name = models.CharField(max_length=30, unique=True)
    
    def __str__(self):
        return f"{self.name}"