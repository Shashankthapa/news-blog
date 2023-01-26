from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from .models import Category, NewsPage
from django.contrib.auth.models import User
from django.contrib import messages
from datetime import datetime
import os


# Create your views here.


@login_required(login_url='/login/')
def news_insert(request):
    if request.method == "POST":
        val = int(request.POST.get('dropdown'))
        title = request.POST['title']
        desc = request.POST['desc']
        date = request.POST['date']
        time = datetime.now().strftime("%H:%M")
        if request.FILES:
            image = request.FILES['image']
        cur_user = User.objects.get(username=request.user)
        NewsPage.objects.create(
            title=title, desc=desc, date=date, cat_id=val, user_name=cur_user, image=image, time=time)
        return redirect('news_insert')
    else:
        data = {

            "cat": Category.objects.all(),
            "news": NewsPage.objects.all()
        }
        return render(request, 'news_insert.html', data)


@login_required(login_url='/login/')
def news_main(request):
    data = {
        "news": NewsPage.objects.all()
    }
    return render(request, 'home_main.html', data)


def one_news(request, slug):
    data = {
        "news": NewsPage.objects.get(news_slug=slug)
    }
    return render(request, "one_news.html", data)


def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        confirmPass = request.POST['confirmPassword']
        if password != confirmPass:
            return HttpResponse('Passwords not same')
        else:
            myUser = User.objects.create_user(
                name, email, password, is_staff=True)
            myUser.save()
            messages.success(request, ("User created successfully"))
            return redirect('/news_main/')
    return render(request, 'register.html')


def login(request):
    if request.method == "POST":
        login_name = request.POST['login_name']
        login_password = request.POST['login_password']
        user = authenticate(request, username=login_name,
                            password=login_password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, "User logged in")
            return redirect('news_main')
        else:
            messages.error(request, "User does not exist")
            return redirect('login')
    else:
        return render(request, 'login.html')


@login_required(login_url='/login/')
def user_logout(request):
    logout(request)
    messages.success(request, ("You were logged out!"))
    return redirect('login')


@login_required(login_url='/login/')
def add_categories(request):
    if request.method == "POST":
        name = request.POST['category']
        Category.objects.create(cat=name)
        messages.success(request, ("Category added successfully"))
        return redirect('add_categories')
    else:
        return render(request, 'categories.html')


@login_required(login_url='/login/')
def edit_news(request, slug):
    if request.method == "POST":
        update = NewsPage.objects.get(news_slug=slug)
        update.cat = request.POST.get('cat')
        update.title = request.POST['title']
        update.desc = request.POST['desc']
        if request.FILES:
            update.image = request.FILES['image']
        update.time = datetime.now().strftime("%H:%M")
        update.date = request.POST['date']
        update.save()
        messages.success(request, "Updated successfully.")
        return redirect('news_main')
    else:
        data = {
            "news_obj": NewsPage.objects.get(news_slug=slug),
            "cat_obj": Category.objects.all()
        }
        return render(request, "edit_news.html", data)


def delete_file(file_name):
    path = os.getcwd() + "/media/" + str(file_name)
    if os.path.exists(path):
        os.remove(path)
        return True
    else:
        return False


def delete_news(request, slug):
    news_obj = NewsPage.objects.get(news_slug=slug)
    if delete_file(news_obj.image) and news_obj.delete():
        messages.error(request, "Your file is deleted successfully")
        return redirect('news_main')
    else:
        messages.error(request, "You had some error")
        return redirect('news_main')
