# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect
from models import User

# Create your views here.
def index(request):
    return render(request, 'lr_templates/index.html')

def register(request):
    results = User.objects.register_validator(request.POST)
    print results
    if results[0]:
        request.session['user_id'] = results[1].id
        print 'You registered!'
        return redirect("/wishlist_app/")
    else:
        for err in results[1]:
            messages.error(request, err)
        return redirect('/lr_app')

def login(request):
    results = User.objects.login_validator(request.POST)
    print results
    if results[0]:
        request.session['user_id'] = results[1].id
        print 'You logged in!'
        return redirect("/wishlist_app/")
    else:
        for err in results[1]:
            messages.error(request, err)
        return redirect('/lr_app')

def logout(request):
    request.session.clear()
    return redirect('/lr_app')