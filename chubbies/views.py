from django.shortcuts import render
from django.http import HttpResponse
from chubbies.models import *

# Create your views here.
def index(request):
    chubbies = Chubbie.objects.all()
    return render(request, 'base.html', {
            'chubbies': chubbies,
    })

def category(request, category):
    chubbies = Chubbie.objects.filter(category=category)
    return render(request, 'category.html', {
            'chubbies': chubbies,
    })
