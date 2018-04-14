from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    todos =  { 'todos_page': 'and I also write some javascript web LANGUAGE_CODE'}
    return render(request, "todos/index.html", context = todos)

def index(request):
    my_contact = { 'home_page' : 'This is the home page. Welcome feel free to take a look.'}
    return render(request, "todos/home.html", context  = my_contact)

def vlog(request):
    my_vlog = {'first_vlog': 'This vlog page will allow you to comments and leave feedback.'}
    return render(request, "todos/vlog.html", context = my_vlog)
