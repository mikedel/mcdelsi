from django.shortcuts import render
from django.http import HttpResponse
from chubbies.models import *

# Create your views here.
def index(request):
    chubbies = Chubbie.objects.all()
    return render(request, 'base.html', {
            'chubbies': chubbies,
    })
    return HttpResponse("Hello, world. You're at Mcdelsi Used Chubbies.")

def category(request, category):
    return HttpResponse("Category " + category)
