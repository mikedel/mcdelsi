from django.shortcuts import render, redirect
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
            'category': category,
    })

def product(request, product):
    chubbie = Chubbie.objects.get(slug=product)
    return render(request, 'product.html', {
            'chubbie': chubbie,
    })

def added(request, product):
    if request.session.get('chubbies', []):
        request.session['chubbies'].append(product)
        request.session.modified = True
    else:
        request.session['chubbies'] = [product]
    return redirect('/cart/')

def deleted(request, product):
    if request.session.get('chubbies', []):
        request.session['chubbies'].remove(product)
        request.session.modified = True
    else:
        request.session['chubbies'] = []
    return redirect('/cart/')

def cart(request):
    slugs = request.session.get('chubbies', [])
    chubbies = []
    total = 0.0
    for slug in slugs:
        chubbie = Chubbie.objects.get(slug=slug)
        chubbies.append(chubbie)
        total += float(chubbie.price)
    return render(request, 'cart.html', {
            'chubbies': chubbies,
            'total': total,
    })

def checkout(request):
    slugs = request.session.get('chubbies', [])
    chubbies = []
    total = 0.0
    for slug in slugs:
        chubbie = Chubbie.objects.get(slug=slug)
        chubbies.append(chubbie)
        total += float(chubbie.price)
    return render(request, 'checkout.html', {
            'chubbies': chubbies,
            'total': total,
    })

def order_confirmation(request):
    slugs = request.session.get('chubbies', [])
    chubbies = []
    for slug in slugs:
        chubbies.append(Chubbie.objects.get(slug=slug))
    if slugs:
        request.session['chubbies'] = []
        request.session.modified = True
    return render(request, 'order_confirmation.html', {
            'chubbies': chubbies,
    })

