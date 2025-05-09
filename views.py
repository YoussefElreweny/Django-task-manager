from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('task_list')
    else:
        form = UserCreationForm()
    return render(request, 'tasks/signup.html', {'form': form})
