from django.contrib import admin
from .models import Employee, Tool, TechBox

# Register your models here.

admin.site.register(Employee)
admin.site.register(Tool)
admin.site.register(TechBox)