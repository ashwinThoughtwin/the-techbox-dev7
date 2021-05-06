from django.shortcuts import render, HttpResponseRedirect, redirect
from django.views.decorators.csrf import csrf_exempt
from .forms import AddToolForm, AddEmployeeForm, IssueToolForm, UpdateToolForm
from django.contrib.auth.decorators import login_required
from .models import TechBox, Employee, IssueGadget
from django.urls import reverse
from django.core.mail import send_mail
from Tech_Box_Project.settings import EMAIL_HOST_USER
from django.http import JsonResponse
from django.views.generic.base import TemplateView
from .tasks import send_confirm_email_task, send_remember_email_task
from django.utils.decorators import method_decorator
from django.views import View
import stripe
from django.conf import settings
from django.views.decorators.cache import cache_page

# Create your views here.

stripe.api_key = settings.STRIPE_SECRET_KEY

YOUR_DOMAIN = 'http://localhost:8000'

class CreateCheckoutSessionView(View):
    def post(self, *args, **kwargs):
        product_id = self.kwargs["pk"]
        product = TechBox.objects.get(id=product_id)
        print(product)
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'inr',
                        'unit_amount': product.price * 100,
                        'product_data': {
                            'name': product.name,
                            # 'images': ['https://i.imgur.com/EHyR2nP.png'],
                        },
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/gadgets/success',
            cancel_url=YOUR_DOMAIN + '/gadgets/cancel',
        )
        return JsonResponse({'id': checkout_session.id})


class ProductLandingPageView(TemplateView):
    template_name = "app_gadgets/landing.html"

    def get_context_data(self, **kwargs):
        id = self.kwargs['pk']
        print(kwargs)
        context = super().get_context_data(**kwargs)
        context['STRIPE_PUBLIC_KEY'] = settings.STRIPE_PUBLIC_KEY
        context['product'] = TechBox.objects.get(id=id)
        return context


class SuccessView(TemplateView):
    template_name = 'app_gadgets/success.html'


class CancelView(TemplateView):
    template_name = 'app_gadgets/cancel.html'


decorators = [login_required]


@method_decorator(decorators, name="dispatch")
class DashboardView(TemplateView):
    template_name = 'app_gadgets/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gadget_count'] = TechBox.objects.count()
        context['employee_count'] = Employee.objects.count()
        context['emp_data'] = Employee.objects.all()
        context['gadget_data'] = TechBox.objects.all()
        context['issue_gadget_count'] = IssueGadget.objects.count()
        context['form'] = AddEmployeeForm()
        context['issued_gadget_data'] = IssueGadget.objects.all()
        context['available_gadget'] = context['gadget_count'] - context['issue_gadget_count']
        return context


@method_decorator(login_required, name="dispatch")
class AddToolView(View):
    def get(self, request):
        form = AddToolForm()
        return render(request, "app_gadgets/addgadget.html", context={'form': form})

    def post(self, request):
        form = AddToolForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("app_gadgets:dashboard"))


@method_decorator(login_required, name="dispatch")
class AddEmployeeView(View):
    def get(self, request):
        form = AddEmployeeForm()
        return render(request, "app_gadgets/addemp.html", context={'form': form})

    def post(self, request):
        form = AddEmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("app_gadgets:dashboard"))


@login_required
def addemp_ajax(request):
    print(request.POST)
    form = AddEmployeeForm(request.POST)
    # import pdb;pdb.set_trace()
    if form.is_valid():
        form.save()
        name = request.POST["name"]
        emp_code = request.POST["emp_code"]
        dept = request.POST["department"]
        city = request.POST["city"]
        phone = request.POST["phone"]
        emp_data = Employee.objects.get(emp_code=int(emp_code))

        data = {'emp': emp_data}

        return render(request, 'app_gadgets/newempdata.html', data)


@method_decorator(login_required, name="dispatch")
class UpdateEmployeeView(View):
    def get(self, request, code):
        emp = Employee.objects.get(emp_code=code)
        form = AddEmployeeForm(instance=emp)
        return render(request, 'app_gadgets/updateemp.html', context={'form': form})

    def post(self, request, code):
        emp = Employee.objects.get(emp_code=code)
        form = AddEmployeeForm(request.POST, instance=emp)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("app_gadgets:dashboard"))


decorator = [login_required, csrf_exempt]


@method_decorator(decorator, name="dispatch")
class DeleteEmployeeView(View):
    def post(self, request):
        emp_code = request.POST.get('emp_code')
        print(emp_code)
        emp_data = Employee.objects.get(emp_code=emp_code)
        emp_data.delete()
        return JsonResponse({"response": 1})


class IssueGadgetView(View):
    def get(self, request):
        form = IssueToolForm()
        return render(request, 'app_gadgets/issuetool.html', context={'form': form})

    def post(self, request):
        x = request.POST.get('name')
        recipient = request.POST.get('email')
        selected_gadget = TechBox.objects.get(pk=x)
        if selected_gadget.available:
            # import pdb;pdb.set_trace()
            subject = "Regarding Borrowing Gadgets From TechBox."
            subject1 = "Regarding Returning of gadget that is Issued to you."
            message = f"{selected_gadget.name} is issued to {recipient}"
            message1 = f"Returning date of {selected_gadget.name} has reached.kindly return the gadget on time."
            data = IssueGadget.objects.create(gadget_name=TechBox.objects.get(name=selected_gadget.name),
                                              emp_code=request.POST.get('emp_code'))
            # print(data.expire_date)
            expire_date = data.expire_date
            # send_confirm_email_task.delay(subject, message, recipient)
            # send_remember_email_task.delay(subject1, message1, recipient, expire_date)
            # send_remember_email_task.apply_async((subject1, message1, recipient, expire_date), countdown=300)

            send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)
            return JsonResponse({"response": "Available"})
        else:
            return JsonResponse({"response": "Not Available"})


@method_decorator(login_required, name="dispatch")
class UpdateTechboxView(View):
    def get(self, request, id):
        data = TechBox.objects.get(id=id)
        form = UpdateToolForm(instance=data)
        return render(request, 'app_gadgets/updatetool.html', context={'form': form})

    def post(self, request, id):
        data = TechBox.objects.get(id=id)
        form = UpdateToolForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("app_gadgets:gadget_table"))


decorator = [login_required, csrf_exempt]


@method_decorator(decorator, name="dispatch")
class GadgetTableView(TemplateView):
    template_name = 'app_gadgets/gadget_table.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gadget_data'] = TechBox.objects.all()
        return context

    def post(self, request):
        gadget_id = request.POST.get('gadget_id')
        print(gadget_id)
        gadget_data = TechBox.objects.get(id=gadget_id)
        gadget_data.delete()
        return JsonResponse({"response": 1})


@method_decorator(login_required, name="dispatch")
class IssueTableView(TemplateView):
    template_name = 'app_gadgets/issue_table.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issued_gadget_data'] = IssueGadget.objects.all()
        return context


class IndexView(TemplateView):
    template_name = "app_gadgets/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['STRIPE_PUBLIC_KEY'] = settings.STRIPE_PUBLIC_KEY
        return context


def charge(request):
    if request.method == 'POST':
        print('Data:', request.POST)

        amount = int(request.POST['amount'])

        customer = stripe.Customer.create(
            email=request.POST['email'],
            name=request.POST['username'],
            address={
                'line1': '510 Townsend St',
                'postal_code': '98140',
                'city': 'San Francisco',
                'state': 'CA',
                'country': 'US',
            },
            source=request.POST['stripeToken']
        )

        charge = stripe.Charge.create(
            customer=customer,
            amount=amount * 100,
            currency='inr',
            description="Donation"
        )

    return HttpResponseRedirect(reverse('app_gadgets:success', args=[amount]))


def successMsg(request, args):
    amount = args
    return render(request, 'app_gadgets/success.html', {'amount': amount})


# ---------------------------FUNCTION BASED VIEWS-------------------------------------------------------------

# @login_required
# def dashboard_view(request):
#     form = AddEmployeeForm()
#     gadget_count = TechBox.objects.count()
#     employee_count = Employee.objects.count()
#     issue_gadget_count = IssueGadget.objects.count()
#     available_gadget = gadget_count - issue_gadget_count
#     emp_data = Employee.objects.all()
#     gadget_data = TechBox.objects.all()
#     issued_gadget_data = IssueGadget.objects.all()
#
#     return render(request, 'app_gadgets/dashboard.html',
#                   context={'gadget_count': gadget_count, 'employee_count': employee_count, 'emp_data': emp_data,
#                            'gadget_data': gadget_data, 'issue_gadget_count': issue_gadget_count,
#                            'available_gadget': available_gadget, 'issued_gadget_data': issued_gadget_data, 'form': form})


# @login_required
# def addtool_view(request):
#     form = AddToolForm()
#     if request.method == "POST":
#         form = AddToolForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse("app_gadgets:dashboard"))
#
#     return render(request, "app_gadgets/addgadget.html", context={'form': form})


# @login_required
# def tool_list(request):
#     # import pdb;pdb.set_trace()
#     data = TechBox.objects.all()
#     return render(request, "app_gadgets/toollist.html", context={'data': data})


# @login_required
# def addemp_view(request):
#     form = AddEmployeeForm()
#     if request.method == "POST":
#         form = AddEmployeeForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse("app_gadgets:dashboard"))
#
#     return render(request, "app_gadgets/addemp.html", context={'form': form})


# @login_required
# def update_emp_view(request, code):
#     emp = Employee.objects.get(emp_code=code)
#
#     form = AddEmployeeForm(instance=emp)
#
#     if request.method == "POST":
#         form = AddEmployeeForm(request.POST, instance=emp)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse("app_gadgets:dashboard"))
#
#     return render(request, 'app_gadgets/updateemp.html', context={'form': form})


# @login_required
# def delete_emp_view(request, code):
#     emp = Employee.objects.get(emp_code=code)
#     emp.delete()
#     return HttpResponseRedirect(reverse("app_gadgets:dashboard"))


# @login_required
# @csrf_exempt
# def delete_emp_view(request):
#     if request.method == "POST":
#         emp_code = request.POST.get('emp_code')
#         print(emp_code)
#         emp_data = Employee.objects.get(emp_code=emp_code)
#         emp_data.delete()
#         return JsonResponse({"response": 1})
#     else:
#         return JsonResponse({"response": 0})


# @login_required
# def issue_gadget_view(request):
#     form = IssueToolForm()
#     if request.method == "POST":
#         x = request.POST.get('name')
#         recipient = request.POST.get('email')
#         selected_gadget = TechBox.objects.get(pk=x)
#         if selected_gadget.available:
#             # import pdb;pdb.set_trace()
#             subject = "Regarding Borrowing Gadgets From TechBox."
#             subject1 = "Regarding Returning of gadget that is Issued to you."
#             message = f"{selected_gadget.name} is issued to {recipient}"
#             message1 = f"Returning date of {selected_gadget.name} has reached.kindly return the gadget on time."
#             data = IssueGadget.objects.create(gadget_name=TechBox.objects.get(name=selected_gadget.name), emp_code=request.POST.get('emp_code'))
#             # print(data.expire_date)
#             expire_date = data.expire_date
#             send_confirm_email_task.delay(subject, message, recipient)
#             send_remember_email_task.delay(subject1, message1, recipient, expire_date)
#             # send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)
#             return JsonResponse({"response": "Available"})
#         else:
#             return JsonResponse({"response": "Not Available"})
#     return render(request, 'app_gadgets/issuetool.html', context={'form': form})


# @login_required
# def update_Techbox_View(request, id):
#     data = TechBox.objects.get(id=id)
#     form = UpdateToolForm(instance=data)
#
#     if request.method == "POST":
#         form = UpdateToolForm(request.POST, instance=data)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse("app_gadgets:gadget_table"))
#
#     return render(request, 'app_gadgets/updatetool.html', context={'form': form})


# def gadget_table_view(request):
#     gadget_data = TechBox.objects.all()
#     return render(request, 'app_gadgets/gadget_table.html', context={'gadget_data': gadget_data})


# def issue_table_view(request):
#     issued_gadget_data = IssueGadget.objects.all()
#     return render(request, 'app_gadgets/issue_table.html', context={'issued_gadget_data': issued_gadget_data})


# customer = stripe.Customer.create(
        #     name='Jenny Rosen',
        #     address={
        #         'line1': '510 Townsend St',
        #         'postal_code': '98140',
        #         'city': 'San Francisco',
        #         'state': 'CA',
        #         'country': 'US',
        #     },
        #     source=request.POST['stripeToken'],
        # )