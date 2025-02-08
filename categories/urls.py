from django.urls import path
from categories import views

urlpatterns = [
    path('categories/', views.CategoryListView.as_view()), 
]