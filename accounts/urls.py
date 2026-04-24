from django.urls import path
from . import views

urlpatterns = [
   path('',views.home, name='home'),
   path('accounts/register/',views.register_view, name='register'),
   path('accounts/login/',views.login_view, name='login'),
   path('accounts/logout/',views.logout_view, name='logout'),
   path('searched/',views.user_searching, name='search'),
]
