from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def fns(request):
    return HttpResponse("rahil are you okay")
def fnhome(request):
    return render(request,'home.html')