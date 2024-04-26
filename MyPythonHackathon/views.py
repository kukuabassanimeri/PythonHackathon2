from django.shortcuts import render
import random
# Create your views here.


def python(request):
    return render(request, 'python.html')