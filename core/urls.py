from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('addresses/new/', views.create_address, name='create_address'),
    path('addresses/', views.list_addresses, name='list_addresses'),
    path('orders/new/<int:address_id>/', views.create_order, name='create_order'),
]

