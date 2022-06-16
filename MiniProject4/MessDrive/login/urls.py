from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('signin/', views.signin, name = "signin"),
    path('inmate_register/', views.inmate_register.as_view(), name = "inmate_register"),
    path('staff_register/', views.staff_register.as_view(), name = "staff_register"),


    
]
