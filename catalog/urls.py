from django.urls import path
from . import views

urlpatterns = [
path('',views.testpage, name='login')
path('testpage/', views.testpage, name='testpage'),
]
