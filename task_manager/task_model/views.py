from django.shortcuts import render,redirect
from . import models
from . import forms
# Create your views here.
def task_view(request):
    if request.method == 'POST':
        task_form = forms.taskform(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect('home')
    else:
         task_form = forms.taskform()
    return render(request, 'task.html',{'task_form':task_form})

def edit(request,id):
    task = models.task.objects.get(pk=id)
    task_form = forms.taskform(instance=task)
    if request.method == 'POST':
        task_form = forms.taskform(request.POST,instance=task)
        if task_form.is_valid():
            task_form.save()
            return redirect('home')
    return render(request, 'task.html',{'task_form':task_form})

def delete(id):
    task = models.task.objects.get(pk=id)
    task.delete()