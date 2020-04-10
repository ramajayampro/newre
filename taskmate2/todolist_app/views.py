from django.shortcuts import render, redirect
from django.http import HttpResponse
from todolist_app.models import Tasklist
from todolist_app.froms import TaskForm
from django.contrib import messages



# Create your views here.



def todolist(request):
          if request.method == "POST":
               form = TaskForm(request.POST or None)
               if form.is_valid():
                    form.save()
                    messages.success(request,("New Task Added Successfully!"))     
                    return  redirect('todolist')          
          else:
                all_tasks = Tasklist.objects.all()
                all_tasks_sorted = Tasklist.objects.order_by('fstatus')
                return render(request, 'todolist.html', {'all_tasks': all_tasks_sorted})


def edit_task(request, task_id):
     if request.method == "POST":
               task = Tasklist.objects.get(pk=task_id)
               form = TaskForm(request.POST or None, instance = task)
               if form.is_valid():
                    form.save()   

               messages.success(request,("Task Edited "))     
               return  redirect('todolist')
     else:
          task_obj = Tasklist.objects.get(pk=task_id)
          return render(request, 'edit.html', {'task_obj': task_obj})


def view_task(request, task_id):
          task_obj = Tasklist.objects.get(pk=task_id)
          return render(request, 'viewlogs.html', {'task_obj': task_obj})

def complete_task(request):

          all_tasks = Tasklist.objects.all()
          all_tasks_sorted = Tasklist.objects.filter(fstatus=True).order_by('fstatus')
          return render(request, 'complete.html', {'all_tasks': all_tasks_sorted})

def finish1_task(request, task_id):
          task = Tasklist.objects.get(pk=task_id)
          task.fstatus = True
          task.status = "Approval"
          task.save()
          messages.success(request,("Task marked as Complete"))
          return  redirect('finish_task')

def finish_task(request):
     all_tasks = Tasklist.objects.all()
     all_tasks_sorted = Tasklist.objects.filter(status="Approval").order_by('fstatus')
     return render(request, 'finish.html', {'all_tasks': all_tasks_sorted})





