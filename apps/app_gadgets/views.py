from django.shortcuts import render, HttpResponseRedirect
from .forms import AddToolForm, AddEmployeeForm, IssueToolForm, UpdateToolForm
from django.contrib.auth.decorators import login_required
from .models import TechBox, Employee, IssueGadget
from django.http import HttpResponse
from django.urls import reverse
# Create your views here.

@login_required
def dashboard_view(request):
    gadget_count = TechBox.objects.count()
    employee_count = Employee.objects.count()
    issue_gadget_count = IssueGadget.objects.count()
    available_gadget = gadget_count - issue_gadget_count
    emp_data = Employee.objects.all()
    gadget_data = TechBox.objects.all()
    issued_gadget_data = IssueGadget.objects.all()

    return render(request, 'app_gadgets/dashboard.html',
                  context={'gadget_count': gadget_count, 'employee_count': employee_count, 'emp_data': emp_data,
                           'gadget_data': gadget_data, 'issue_gadget_count': issue_gadget_count,
                           'available_gadget': available_gadget, 'issued_gadget_data': issued_gadget_data})


@login_required
def addtool_view(request):
    form = AddToolForm()
    if request.method == "POST":
        form = AddToolForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("app_gadgets:dashboard"))

    return render(request, "app_gadgets/addgadget.html", context={'form': form})


# @login_required
# def tool_list(request):
#     # import pdb;pdb.set_trace()
#     data = TechBox.objects.all()
#     return render(request, "app_gadgets/toollist.html", context={'data': data})


@login_required
def addemp_view(request):
    form = AddEmployeeForm()
    if request.method == "POST":
        form = AddEmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("app_gadgets:dashboard"))

    return render(request, "app_gadgets/addemp.html", context={'form': form})


@login_required
def update_emp_view(request, code):
    emp = Employee.objects.get(emp_code=code)

    form = AddEmployeeForm(instance=emp)

    if request.method == "POST":
        form = AddEmployeeForm(request.POST, instance=emp)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("app_gadgets:dashboard"))

    return render(request, 'app_gadgets/updateemp.html', context={'form': form})


@login_required
def delete_emp_view(request, code):
    emp = Employee.objects.get(emp_code=code)
    emp.delete()
    return HttpResponseRedirect(reverse("app_gadgets:dashboard"))


@login_required
def issue_gadget_view(request):
    form = IssueToolForm()
    if request.method == "POST":
        # print(request.POST)
        # x = request.POST.get('gadget_name')
        # print(x)
        x = request.POST.get('gadget_name')
        selected_gadget = TechBox.objects.get(pk=x)

        if selected_gadget.available:
            form = IssueToolForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse("app_gadgets:dashboard"))
        else:
            return HttpResponse("Not Available.")

    return render(request, 'app_gadgets/issuetool.html', context={'form': form})


@login_required
def update_Techbox_View(request, id):
    data = TechBox.objects.get(id=id)
    form = UpdateToolForm(instance=data)

    if request.method == "POST":
        form = UpdateToolForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("app_gadgets:dashboard"))

    return render(request, 'app_gadgets/updatetool.html', context={'form': form})