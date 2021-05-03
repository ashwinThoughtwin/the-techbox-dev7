from django.contrib import admin
from .models import Employee, IssueGadget, TechBox

# Register your models here.

# admin.site.register(Employee)
# admin.site.register(IssueGadget)
# admin.site.register(TechBox)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'emp_code', 'department', 'address', 'city', 'phone', 'date_joined')


@admin.register(TechBox)
class TechBoxAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'available')


@admin.register(IssueGadget)
class IssueGadgetAdmin(admin.ModelAdmin):
    list_display = ('id', 'gadget_name', 'emp_code', 'issue_date', 'expire_date')