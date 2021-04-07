"""todolist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from todolist_app import views
from todolist_app.views import TodoListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TodoListView.as_view(), name='todo_list'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('create/', views.TodoCreateView.as_view(), name='create_todo'),
    path('create_priority/', views.PriorityCreateView.as_view(), name='create_priority'),
    path('update/<int:pk>/', views.TodoUpdateView.as_view(), name='edit_todo'),
    path('update_assigned/<int:pk>/', views.TodoAssignedUpdateView.as_view(), name='update_todo_assigned'),
    path('delete/<int:pk>/', views.TodoDeleteView.as_view(), name='delete_todo'),
]
