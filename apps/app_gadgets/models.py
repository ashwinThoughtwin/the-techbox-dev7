from django.db import models
from datetime import datetime, timedelta

# Create your models here.

class Employee(models.Model):
    dept_choice = [
        ('python', 'Python'),
        ('reactjs', 'ReactJS'),
        ('ror', 'ROR'),
        ('bd', 'Business Development')
    ]

    city_choice = [
        ('neemuch', 'Neemuch'),
        ('indore', 'Indore')
    ]
    name = models.CharField(max_length=60, blank=False)
    email = models.EmailField(unique=True,null=False, blank=False)
    department = models.CharField(max_length=40, choices=dept_choice, default='python')
    address = models.TextField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=100, choices=city_choice, default='indore')
    phone = models.CharField(max_length=20, blank=False)
    date_joined = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.name) + " " + str(self.email)


def exp_date():
    return datetime.today() + timedelta(days=10)


class Tool(models.Model):
    tool_choice = [
        ('headphone', 'Headphone'),
        ('cpu', 'CPU'),
        ('mouse', 'Mouse'),
        ('connector', '2 Way Connector'),
        ('monitor', 'Monitor'),
        ('charger', 'Charger')
    ]
    name = models.CharField(max_length=30, choices=tool_choice, default='headphone')
    issue_date = models.DateField(auto_now=True)
    expire_date = models.DateField(default=exp_date)
    borrower = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.name) + " " + str(self.borrower)

