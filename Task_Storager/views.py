from django.shortcuts import render,redirect
from .models import Tasks
import datetime
from django.contrib import admin,messages
# from django.utils import timezone
# Create your views here.
admin.site.register(Tasks)


# time_24h_str = formatted_time.strftime()
def index(request):
    retrived_data=Tasks.objects.all()
    return render(request,"index.html",{'Datas':retrived_data})
def update(request):
    if request.method=="POST":
        id=request.POST['id']
        retrived_data=Tasks.objects.get(id=id)
        print(id)
        print(retrived_data.Task_Name)
        return render(request,"index.html",{'updateDatas':retrived_data})
def updatedata(request,id):
        if request.method=='POST':  
            # id=request.POST['id']
            retrived_data=Tasks.objects.get(id=id)
            task_get=request.POST["task_name"]
            retrived_data.Task_Name=task_get
            retrived_data.save()
            return redirect("home")
def add(request):
    if request.method=="POST":
        current_time=datetime.datetime.now()
        formatted_time=current_time.strftime("%H:%M")
        Time_get=formatted_time
        Task_get=request.POST['task']
        if not Task_get.strip():
            messages.warning(request,"Warning: Please enter the Task")
            return redirect("home")
        if Task_get.isspace():
            messages.warning(request,"Warning: Please enter the Task")
            return redirect("home")
        else:
            obj=Tasks()
            obj.Time=Time_get
            obj.Task_Name=Task_get
            obj.save()
            messages.success(request,"Task added")
    return redirect("home")
def delete(request,id):
    retrived_data=Tasks.objects.get(id=id)
    retrived_data.delete()
    return redirect("home")
# def uvarajan(request):
#     return redirect("www.linkedin.com/in/uvarajan-dev")