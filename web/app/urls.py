from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('b/<str:pk>/', views.benches, name="benches"),
    path('b/', views.benchlist, name="bench-list"),
    path('create/', views.CreateBench, name="create"),
]
