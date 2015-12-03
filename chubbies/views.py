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

def product(request, product):
    chubbie = Chubbie.objects.get(name=product)
    return render(request, 'product.html', {
            'chubbie': chubbie,
    })

def added(request, product):
    if request.session.get('chubbies', ''):
        request.session['chubbies'].append(product)
        request.session.modified = True
    else:
        request.session['chubbies'] = [product]
    return HttpResponse("added to cart" + product + " Session: " + str(request.session.get('chubbies', '')))
