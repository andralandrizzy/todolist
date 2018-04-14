from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('media/', views.home, name  = 'home'),
    path('vlog/', views.vlog, name = 'vlog'),
]
