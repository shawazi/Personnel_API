from django.contrib import admin
from .models import Personnel, Department

# Register your models here.

admin.site.register((Personnel, Department))