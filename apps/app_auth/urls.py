from django.urls import path
from . import views

app_name = "app_auth"

urlpatterns = [

    path('', views.AdminLoginView.as_view(), name="login"),
    path('logout/', views.logout_user, name="logout"),
]

# path('', views.login_user, name="login"),