from django.urls import path
from . import views
from . import api_views
from rest_framework.authtoken.views import obtain_auth_token


app_name = "app_gadgets"

urlpatterns = [

    path('addtool/', views.AddToolView.as_view(), name="addtool"),
    path('addemp/', views.AddEmployeeView.as_view(), name="addemp"),
    path('update_emp/<int:code>', views.UpdateEmployeeView.as_view(), name="update_emp"),
    path('delete_emp/', views.DeleteEmployeeView.as_view(), name="delete_emp"),
    path('issue_gadget/', views.IssueGadgetView.as_view(), name="issue_gadget"),
    path('update_techbox/<int:id>', views.UpdateTechboxView.as_view(), name="update_techbox"),
    path('dashboard/', views.DashboardView.as_view(), name="dashboard"),
    path('add_emp/', views.addemp_ajax, name="add_emp"),
    path('gadget_table/', views.GadgetTableView.as_view(), name="gadget_table"),
    path('issue_table/', views.IssueTableView.as_view(), name="issue_table"),

    path('gadget_api/', api_views.TechBoxAPI.as_view(), name='gadget_api'),
    path('gadget_api/<int:pk>/', api_views.TechBoxAPI.as_view(), name='gadget_api'),

    path('issue_gadget_api/', api_views.IssueGadgetAPI.as_view(), name='issue_gadget_api'),

    path('gettoken/', obtain_auth_token),

    path('product_landing_page/<pk>', views.ProductLandingPageView.as_view(), name="product_landing_page"),

    path('create-checkout-session/<pk>/', views.CreateCheckoutSessionView.as_view(), name="create-checkout-session"),

    path('cancel/', views.CancelView.as_view(), name="cancel"),
    path('success/', views.SuccessView.as_view(), name="success"),


]

# urlpatterns = [
#     # path('addtool/', views.addtool_view, name="addtool"),
#     path('addtool/', views.AddToolView.as_view(), name="addtool"),
#     # path('toollist', views.tool_list, name="toollist"),
#     # path('addemp/', views.addemp_view, name="addemp"),
#     path('addemp/', views.AddEmployeeView.as_view(), name="addemp"),
#     # path('update_emp/<int:code>', views.update_emp_view, name="update_emp"),
#     path('update_emp/<int:code>', views.UpdateEmployeeView.as_view(), name="update_emp"),
#     # path('delete_emp/<int:code>', views.delete_emp_view, name="delete_emp"),
#     # path('delete_emp/', views.delete_emp_view, name="delete_emp"),
#     path('delete_emp/', views.DeleteEmployeeView.as_view(), name="delete_emp"),
#     # path('issue_gadget/', views.issue_gadget_view, name="issue_gadget"),
#     path('issue_gadget/', views.IssueGadgetView.as_view(), name="issue_gadget"),
#     # path('update_techbox/<int:id>', views.update_Techbox_View, name="update_techbox"),
#     path('update_techbox/<int:id>', views.UpdateTechboxView.as_view(), name="update_techbox"),
#     # path('dashboard/', views.dashboard_view, name="dashboard"),
#     path('dashboard/', views.DashboardView.as_view(), name="dashboard"),
#     path('add_emp/', views.addemp_ajax, name="add_emp"),
#     # path('gadget_table/', views.gadget_table_view, name="gadget_table"),
#     path('gadget_table/', views.GadgetTableView.as_view(), name="gadget_table"),
#     # path('issue_table/', views.issue_table_view, name="issue_table"),
#     path('issue_table/', views.IssueTableView.as_view(), name="issue_table"),
#
# ]