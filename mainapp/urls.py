from django.urls import path
from . import views

urlpatterns = [
    path('mytodos/', views.mytodos, name='mytodos_page'),
    path('contact/', views.contact, name = 'contact_page'),
    path('about/', views.about, name = 'about_page'),
    path('', views.home, name = 'home_page'),
    path('donate/', views.donate, name='donate_page'),
]