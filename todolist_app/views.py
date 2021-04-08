from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from todolist_app.models import Todo, Priority
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class TodoListView(ListView):
    model = Todo

class TodoCreateView(LoginRequiredMixin, CreateView):
    model = Todo
    fields = [
        'description',
        'done',
        'priority',
    ]

    def form_valid(self, form):
        form.instance.user_assigned = self.request.user
        return super().form_valid(form)
        
    success_url = reverse_lazy('todo_list')

class PriorityCreateView(CreateView):
    model = Priority
    fields = '__all__'
    success_url = reverse_lazy('todo_list')

class TodoUpdateView(LoginRequiredMixin, UpdateView):
    model = Todo
    fields = [
        'description',
        'done',
        'priority',
    ]
    success_url = reverse_lazy('todo_list')

class TodoAssignedUpdateView(LoginRequiredMixin, UpdateView):
    model = Todo
    fields = ['user_assigned']
    success_url = reverse_lazy('todo_list')

class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy('todo_list')