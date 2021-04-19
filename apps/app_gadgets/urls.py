from django.urls import path
from . import views


app_name = "app_gadgets"

urlpatterns = [
    path('addtool/', views.addtool_view, name="addtool"),
    # path('toollist', views.tool_list, name="toollist"),
    path('addemp/', views.addemp_view, name="addemp"),
    path('update_emp/<int:code>', views.update_emp_view, name="update_emp"),
    path('delete_emp/<int:code>', views.delete_emp_view, name="delete_emp"),
    path('issue_gadget/', views.issue_gadget_view, name="issue_gadget"),
    path('update_techbox/<int:id>', views.update_Techbox_View, name="update_techbox"),
    path('dashboard/', views.dashboard_view, name="dashboard"),

]