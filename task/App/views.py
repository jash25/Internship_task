from django.shortcuts import render,redirect
from .models import *
from _datetime import datetime
username=''
created_at=''
id1=''
def index(request):
    return render(request,'login.html')
def sign_up(request):
    return render(request,'sign_up.html')

def signup(request):
    user = User()
    if request.method == 'POST':
        user.first_name = request.POST.get('fname')
        user.last_name = request.POST.get('lname')
        user.email = request.POST.get('email')
        user.username = request.POST.get('username')
        user.password = request.POST.get('password')
        user.save()
        return render(request,'login.html')
def login(request):
    global username
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username,password=password)
        if user:
            return render(request,'post.html',{'username':username})
        else:
            return redirect('index')
def post_get(request):
    global username,created_at,id1
    post = Post()
    if request.method == 'POST':
        post.text = request.POST.get('text')
        post.created_at = datetime.now()
        post.updated_at = datetime.now()
        created_at = post.created_at
        updated_at = post.updated_at
        text = post.text
        updated_post0(request, text, updated_at, created_at)
        return render(request,'post1.html',{'created_at':created_at,'updated_at':updated_at,'text':text,'username':username})
def updated_post0(request,text,updated_at,created_at):
    global username,id1
    user = User.objects.filter(username = username)
    post,created = Post.objects.get_or_create(user=user[0],text=text,created_at=created_at,updated_at=updated_at)
    post.save()
    id1 = post.id
    return render(request,'post1.html',{'created_at':created_at,'updated_at':updated_at,'text':text,'username':username})

def update_post(request):
    global username,created_at,id1
    user = User.objects.filter(username = username)

    if request.method == 'POST':
        post = Post.objects.get(user=user[0],id=id1)
        post.text = request.POST.get('text')
        post.updated_at = datetime.now()
        post.save()
        created_at = post.created_at
        updated_at = post.updated_at
        text = post.text
        return render(request,'post1.html',{'created_at':created_at,'updated_at':updated_at,'text':text,'username':username})
# Create your views here.
def update(request):
    global username,created_at
    user = User.objects.filter(username=username)

    post = Post.objects.filter(user=user[0]).all().values('id','text','created_at','updated_at')
    return render(request, 'update.html',
                      {'post':post})
def update1(request,id):
    global id1
    id1 = id
    post = Post.objects.get(id=id)
    username = post.user
    text = post.text
    created_at =post.created_at
    updated_at = post.updated_at
    return render(request, 'post1.html',
                  {'created_at': created_at, 'updated_at': updated_at, 'text': text, 'username': username})

def back_post(request):
    global username
    return render(request,'post.html',{'username':username})
