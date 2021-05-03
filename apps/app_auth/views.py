from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse
from django.shortcuts import redirect
from .forms import LoginForm
from django.views import View

# Create your views here.

class AdminLoginView(View):
    def post(self, request):

        username = request.POST.get("username")
        password = request.POST.get("password")


        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("app_gadgets:dashboard"))
        else:
            messages.error(request, 'Username Or Password Not Correct')
            return redirect('app_auth:login')

    def get(self, request):

        if request.user.is_authenticated:
            return redirect("app_gadgets:dashboard")
        return render(request, "app_auth/login.html")



@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse("app_auth:login"))



# def login_user(request):
#     form = LoginForm()
#     if request.user.is_authenticated:
#         return redirect("app_gadgets:dashboard")
#     # gadget_count = TechBox.objects.count()
#     # employee_count = Employee.objects.count()
#     # issue_gadget_count = IssueGadget.objects.count()
#     # available_gadget = gadget_count - issue_gadget_count
#     # emp_data = Employee.objects.all()
#     # gadget_data = TechBox.objects.all()
#     # issued_gadget_data = IssueGadget.objects.all()
#     if request.method == "POST":
#         form = LoginForm(data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get("username")
#             password = form.cleaned_data.get("password")
#
#             user = authenticate(username=username, password=password)
#
#             if user is not None:
#                 login(request, user)
#                 return HttpResponseRedirect(reverse("app_gadgets:dashboard"))
#                 # return render(request, 'app_gadgets/dashboard.html', context={'gadget_count': gadget_count, 'employee_count': employee_count, 'emp_data': emp_data, 'gadget_data': gadget_data, 'issue_gadget_count': issue_gadget_count, 'available_gadget': available_gadget, 'issued_gadget_data': issued_gadget_data})
#     return render(request, "app_auth/login.html", context={'form': form})
