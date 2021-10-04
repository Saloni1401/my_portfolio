from django.contrib import admin

from app.models import Student
from .models import Student

# Register your models here.
admin.site.register(Student)