from django.urls import path
from vehiculo.views import index, CustomLoginView, CustomLogoutView, RegisterView, vehiculoform_view, vehiculolist_view

urlpatterns = [
    path('', index, name='index'),
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('accounts/logout/', CustomLogoutView.as_view(), name='logout'),
    path('accounts/register/', RegisterView.as_view(), name='register'),
    path('vehiculo/add/', vehiculoform_view, name="vehiculo_add"),
    path('vehiculo/list/', vehiculolist_view, name="vehiculo_list"),
    path('login/', CustomLoginView.as_view(), name='login'),
]
