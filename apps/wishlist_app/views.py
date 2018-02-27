# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..lr_app.models import User
from django.shortcuts import render, redirect
from models import Wishlist
from django.contrib import messages

# Create your views here.
def index(request):
    user = User.objects.get(id=request.session['user_id'])
    all_items = Wishlist.objects.all()
    context = {
        'name': user.name,
        'my_items': all_items.filter(contributor=user),
        'my_wishlist': all_items.filter(people_interested=user).exclude(contributor=user),
        'other_items': all_items.exclude(people_interested=user),
    }
    return render(request, 'wishlist_templates/index.html', context)

def add(request):
    return render(request, 'wishlist_templates/add.html')

def save_item(request):
    results = Wishlist.objects.list_validator(request.POST, request.session['user_id'])
    if results[0]:
        request.session['item_id'] = results[1].id
        return redirect('/wishlist_app/')
    else:
        for err in results[1]:
            messages.error(request, err)
        return redirect('/wishlist_app/add')

def wishlist_add(request, item_id):
    i = Wishlist.objects.get(id=item_id)
    u = User.objects.get(id=request.session['user_id'])
    i.people_interested.add(u)
    return redirect('/wishlist_app/')

def wishlist_remove(request, item_id):
    i = Wishlist.objects.get(id=item_id)
    u = User.objects.get(id=request.session['user_id'])
    i.people_interested.remove(u)
    return redirect('/wishlist_app/')

def wishlist_delete(request, item_id):
    Wishlist.objects.get(id=item_id).delete()
    return redirect('/wishlist_app/')


def display(request, item_id):
    list_item = Wishlist.objects.get(id=item_id)
    people_interested = User.objects.filter(items_wanted=item_id)
    context = {
        'item' : list_item.item,
        'people_interested' : people_interested,
    }
    return render(request, 'wishlist_templates/display.html', context)