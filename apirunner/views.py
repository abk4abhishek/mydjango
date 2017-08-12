from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Apirunner
from django.utils import timezone

def runner_list(request):
    #return HttpResponse("Hello, word. You're at the apirunner index.")
    apis=Apirunner.objects.all()
    return render(request, 'apirunner/api_list.html', {'apis':apis})
