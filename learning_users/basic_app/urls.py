from django.urls import path,include
from basic_app import views

app_name = "basic_app"

urlpatterns = [
    path('',views.index,name="index"),
    path('basic_app/register/',views.register,name="register"),
    path('basic_app/login/',views.user_login,name="login"),
    path('basic_app/special/',views.special,name="special"),
    path('basic_app/logout/',views.user_logout,name="logout"),
]
