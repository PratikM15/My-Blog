from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import BlogArticle
# Create your views here.
from django.contrib.auth import authenticate, login, logout

@csrf_exempt
def index(request):
    blogs = BlogArticle.objects.all()
    return render(request, "main.html", {'testvar': "Test String 2!", 'blogs': blogs, 'user': None})

@csrf_exempt
def login_user(request):
    blogs = BlogArticle.objects.all()
    if request.method == 'POST':
        usname = request.POST['username']
        pwd = request.POST['password']
        user = authenticate(username=usname, password=pwd)
        if user is not None:
            login(request, user)
            return render(request, "main.html", {'testvar': "Test String 2!", 'blogs': blogs, 'user': user})
    return render(request, "main.html", {'testvar': "Test String 2!", 'blogs': blogs, 'user': None})

@csrf_exempt
def createBlog(request):
    blogs = BlogArticle.objects.all()
    newBlog = BlogArticle()
    newBlog.title = request.POST['title']
    newBlog.author = request.user
    newBlog.blog_content = request.POST['blog_content']
    newBlog.save()
    return render(request, "main.html", {'testvar': "Test String 2!", 'blogs': blogs, 'user': request.user})

@csrf_exempt
def signup(request):
    blogs = BlogArticle.objects.all()
    if request.method == 'POST':
        usname = request.POST['username1']
        email = request.POST['email']
        pwd = request.POST['password1']
        try:
            user = User.objects.get(email=email)
            if user is not None:
                return render(request, "main.html", {'testvar': "Test String 2!", 'blogs': blogs, 'user': None, 'error': "Email Id already in use."})
        except:
            user = User.objects.create_user(
                username=usname,
                password=pwd,
                email=email
            )
            user.save()
            login(request, user)
            return render(request, "main.html", {'testvar': "Test String 2!", 'blogs': blogs, 'user': user})
    return render(request, "main.html", {'testvar': "Test String 2!", 'blogs': blogs, 'user': None})

def logout_user(request):
    blogs = BlogArticle.objects.all()
    user = request.user
    logout(request)
    return render(request, "main.html", {'testvar': "Test String 2!", 'blogs': blogs, 'user': None})
