from django.urls import path
from tasks import views

urlpatterns = [
    path('tasks/', views.TaskListView.as_view()),
    path('tasks/<int:pk>/', views.TaskDetailView.as_view()),
    path("archive/", views.ArchivedTaskListView.as_view()),
]
