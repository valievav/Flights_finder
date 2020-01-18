from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='search-home'),
    path('about/', views.test_path, name='search-about')  # sub-page for the main page
]



