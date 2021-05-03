from django import forms
from .models import TechBox, Employee, IssueGadget


class AddToolForm(forms.ModelForm):
    name = forms.CharField(max_length=100, label="", widget=forms.TextInput(attrs={'placeholder': 'Enter Gadget Name Here'}))
    class Meta:
        model = TechBox
        fields = ['name']


class AddEmployeeForm(forms.ModelForm):
    name = forms.CharField(max_length=100, label="", widget=forms.TextInput(attrs={'placeholder': 'Enter Name'}))
    emp_code = forms.CharField(max_length=100, label="", widget=forms.TextInput(attrs={'placeholder': 'Enter Emp ID'}))
    email = forms.EmailField(max_length=100, label="", widget=forms.TextInput(attrs={'placeholder': 'Enter Email'}))
    address = forms.CharField(max_length=100, label="", widget=forms.Textarea(attrs={'placeholder': 'Enter Your Address'}))
    phone = forms.CharField(max_length=100, label="", widget=forms.TextInput(attrs={'placeholder': 'Enter Mobile. No.'}))

    class Meta:
        model = Employee
        fields = ['name', 'emp_code', 'email', 'department', 'address', 'city', 'phone']
        labels = {'department': 'Department', 'city': 'Office Location'}


class IssueToolForm(forms.ModelForm):
    emp_code = forms.CharField(max_length=100, label="", widget=forms.TextInput(attrs={'placeholder': 'Enter Emp ID'}, ))
    email = forms.EmailField(max_length=50, label="", widget=forms.EmailInput(attrs={'placeholder':  "Enter Email ID"}))
    class Meta:
        model = IssueGadget
        fields = ['gadget_name', 'email', 'emp_code']
        labels = {'gadget_name': 'Select Gadget'}


class UpdateToolForm(forms.ModelForm):
    class Meta:
        model = TechBox
        fields = ['name', 'available']
        labels = {'name': 'Update Gadget Availability Status'}