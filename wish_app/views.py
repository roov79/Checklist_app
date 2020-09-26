from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages
import bcrypt

### Login and Refistration

def index(request):
    request.session.flush()
    return render(request, 'index.html')

def register(request):
    if request.method == "POST":
        errors =  Users.objects.reg_val(request.POST)
        if  len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect ('/')
        hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        new_user = Users.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=hashed_pw)
        request.session['u_id'] = new_user.id
        return redirect('/wishes')
    return redirect('/')

def login(request):
    if request.method == "POST":
        errors = Users.objects.log_val(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        user = Users.objects.get(email=request.POST['email'])
        request.session['u_id'] = user.id
        return redirect('/wishes')
    return redirect('/')

def wishes(request):
    if 'u_id' not in request.session:
        return redirect('/')
    context = {
        'user': Users.objects.get(id=request.session['u_id']),
        'wish_list': Wishes.objects.filter(wisher=Users.objects.get(id=request.session['u_id'])),
        'granted_list': Wishes.objects.filter(granted=True),
    }
    return render(request, 'home.html', context)

def logout(request):
    request.session.flush()
    return redirect('/')

### Wishing page

def make_wish(request):
    if 'u_id' not in request.session:
        return redirect('/')
    context = {
        'user': Users.objects.get(id=request.session['u_id']),
    }
    return render(request, 'new_wish.html', context)

def add_wish(request):
    if request.method == "POST":
        errors =  Wishes.objects.wish_val(request.POST)
        if  len(errors) != 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect ('/wishes/new')
        Wishes.objects.create(wish=request.POST['wish'], description=request.POST['desc'], wisher=Users.objects.get(id=request.session['u_id']))
        return redirect('/wishes')
    return redirect('/wishes/new')

def edit(request, id):
    if 'u_id' not in request.session:
        return redirect('/')
    context = {
        'user': Users.objects.get(id=request.session['u_id']),
        'wish': Wishes.objects.get(id=id),
    }
    return render(request, 'edit.html', context)

def edit_wish(request, id):
    if request.method == "POST":
        errors =  Wishes.objects.wish_val(request.POST)
        if  len(errors) != 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect (f'/edit/{id}')
        wish = Wishes.objects.get(id=id)
        wish.wish = request.POST['wish']
        wish.description = request.POST['desc']
        wish.save()        
        return redirect('/wishes')
    return redirect(f'/edit/{id}')

def delete_wish(request, id):
    delete_wish = Wishes.objects.get(id=id)
    delete_wish.delete()
    return redirect('/wishes')

def grant_wish(request, id):
    wish = Wishes.objects.get(id=id)
    wish.granted = True
    wish.save() 
    return redirect('/wishes')