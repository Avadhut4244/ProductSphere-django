from django.urls import path
from . import views

app_name = 'electronics'

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_product, name='add_product'),
    path('update_data/<int:id>/', views.update_data, name='update_data'),
    path('delete_data/<int:id>/', views.delete_data, name='deletedata'),
    path('signup/', views.signup_view, name='signup'),
]
