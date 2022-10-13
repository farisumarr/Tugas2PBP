from http.client import HTTPResponse
from django.shortcuts import render
from todolist.models import Task

from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

import datetime
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from django.core import serializers
from django.urls import reverse

from todolist.forms import CreateTaskForm


@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_task = Task.objects.filter(user=request.user)  #data difilter berdasarkan user yang login
    context = {
        'list_task': data_task,
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, "todolist.html", context)

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')

    context = {'form': form}
    return render(request, 'register.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # melakukan login terlebih dahulu
            response = HttpResponseRedirect(
                reverse("todolist:views_ajax"))  # membuat response
            # membuat cookie last_login dan menambahkannya ke dalam response
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/todolist/login/')
def create_task(request):
    form = CreateTaskForm()

    if request.method == "POST":
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            return redirect('todolist:show_todolist')

    context = {'form': form}
    return render(request, 'create-task.html', context)

@login_required(login_url='/todolist/login/')
def show_json(request):
    data_todolist = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', data_todolist))

@login_required(login_url='/todolist/login/')
def add_task_ajax(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        deskripsi = request.POST.get("description")

        new_todolist = Task(title=title, deskripsi=deskripsi, user=request.user)
        new_todolist.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

@login_required(login_url='/todolist/login/')
def views_ajax(request):
    return render(request, "ajax-todolist.html")