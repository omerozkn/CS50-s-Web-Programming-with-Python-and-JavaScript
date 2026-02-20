from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request, "hello/index.html")
def lydia(request):
    return HttpResponse("long live lydia")
def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")
