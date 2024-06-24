from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.user_login_or_register, name='user_register'),

     path('rolelist/', views.RoleList.as_view(), name='role-list'),
      path('check-phone-number/',views.check_phone_number ),
]