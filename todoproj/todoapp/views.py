from django.shortcuts import render, get_object_or_404
from django.contrib import admin
from django.urls import reverse_lazy
from .models import Activity
from .forms import ToDoForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    return render(request, 'todoapp/index.html')


@login_required
def activities_list(request):
    activities_list = Activity.objects.all()
    return render(request, "todo/activities.html", {"activities_list": activities_list})


@login_required
def activityDetail(request, id):
    activity = get_object_or_404(Activity, pk=id)
    return render(request, "todo/activitydetail.html", {"activity": activity})


@login_required
def newActivity(request):
    form = ToDoForm

    if request.method == "POST":
        form = ToDoForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            post.save()
            form = ToDoForm()
    else:
        form = ToDoForm()
    return render(request, "todo/newactivity.html", {'form': form})


def loginmessage(request):
    return render(request, 'todo/loginmessage.html')


def logoutmessage(request):
    return render(request, 'todo/logoutmessage.html')
