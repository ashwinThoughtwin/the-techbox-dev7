from django.contrib import admin
from .models import Employee, IssueGadget, TechBox

# Register your models here.

admin.site.register(Employee)
admin.site.register(IssueGadget)
admin.site.register(TechBox)