from django.urls import path
from . import views


app_name = "app_gadgets"

urlpatterns = [
    path('addtool', views.addtool_view, name="addtool"),
    path('toollist', views.tool_list, name="toollist"),

]