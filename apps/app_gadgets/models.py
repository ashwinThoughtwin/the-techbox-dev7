from django.db import models
from datetime import datetime, timedelta


# Create your models here.

class Employee(models.Model):
    dept_choice = [
        ('Python', 'Python'),
        ('ReactJS', 'ReactJS'),
        ('ROR', 'ROR'),
        ('Business Development', 'Business Development')
    ]

    city_choice = [
        ('Neemuch', 'Neemuch'),
        ('Indore', 'Indore')
    ]
    name = models.CharField(max_length=60, blank=False)
    email = models.EmailField(unique=True,null=False, blank=False)
    emp_code = models.CharField(max_length=10, unique=True)
    department = models.CharField(max_length=40, choices=dept_choice, default='python')
    address = models.TextField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=100, choices=city_choice, default='indore')
    phone = models.CharField(max_length=20, blank=False)
    date_joined = models.DateField(auto_now_add=True)

    # def __str__(self):
    #     return str(self.name) + " " + str(self.email)

    class Meta:
        app_label = 'app_gadgets'

        ordering = ['-emp_code']


class TechBox(models.Model):
    name = models.CharField(max_length=50, blank=False)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "TechBox"

def exp_date():
    return datetime.today() + timedelta(minutes=10)

class IssueGadget(models.Model):
    gadget_name = models.ForeignKey(TechBox, on_delete=models.SET_NULL, null=True)
    issue_date = models.DateField(auto_now=True, null=True)
    expire_date = models.DateTimeField(default=exp_date)
    emp_code = models.CharField(max_length=40)
    # borrower = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = "IssueGadget"




    def __str__(self):
        return str(self.gadget_name) + " " + str(self.emp_code) + " " + str(self.issue_date)


