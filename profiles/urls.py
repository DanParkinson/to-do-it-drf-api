from django.urls import path
from profiles import views

urlpatterns = [
    path('profiles/', views.ProfileListView.as_view()),
    path('profiles/<int:pk>/', views.ProfileDetailView.as_view()),
    path("delete-account/", views.DeleteAccountView.as_view()),
]
