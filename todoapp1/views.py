from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Task

# Create your views here.
def addTask(request):
    new_task=request.POST['task']
    Task.objects.create(task=new_task)
    return redirect('home')

def completed(request,pk):
    task=get_object_or_404(Task,pk=pk)
    task.is_completed=True
    task.save()
    return redirect('home')

def uncompleted(request,pk):
    task=get_object_or_404(Task,pk=pk)
    task.is_completed=False
    task.save()
    return redirect('home')

def editTask(request,pk):
    get_task=get_object_or_404(Task,pk=pk)
    if request.method=='GET':
        context={
            'get_task':get_task
        }
        return render(request,'editTask.html',context)
    else:
        new_task=request.POST['task']
        get_task.task=new_task
        get_task.save()
        return redirect('home')
    
def deleteTask(request,pk):
    get_task=get_object_or_404(Task,pk=pk)
    get_task.delete()
    return redirect('home')
      

   

