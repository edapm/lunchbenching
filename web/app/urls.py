from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('b/<str:pk>/', views.benches, name="benches"),
    path('b/', views.benchlist, name="bench-list"),
    path('create/', views.CreateBench, name="create"),
    path('update/<str:pk>/', views.UpdateBench, name="update"),
    path('delete/<str:pk>/', views.DeleteBench, name="delete"),

    path('login/', views.loginPage, name="login"),
    path('signup/', views.registerPage, name="register"),
    path('logout/', views.logoutUser, name="logout"),

    path('u/<str:slug>/', views.userProfile, name="user"),
    path('update-profile/', views.updateProfile, name="update-profile"),
]
