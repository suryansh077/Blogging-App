from django.shortcuts import render,redirect
from myblog.models import post,User

from PIL import Image
import os

# Create your views here.

def home(request):
     obj = post.objects.all() 
     return render(request, 'home.html',{'obj':obj})
    

def article(request):
    if request.method == "POST":
        title = request.POST['title']
        name = request.POST['name']
        content = request.POST['content']
        img = request.FILES['img']
        my_img = Image.open(img)
        my_path = os.path.join('media/',img.name)
        my_img.save(my_path)

        p = post(title=title, content=content,name=name,img=img.name)
        p.save()

    return render(request, 'article.html')

def edit(request,title):
     obj= post.objects.get(title=title)
     return render(request, 'edit.html',{'obj':obj})

def update(request,title):
    
     up= post.objects.get(title=title)
     up.name = request.POST['name']
     up.title = request.POST['title']
     up.content = request.POST['content']
    
     up.save()
     return redirect('/home')

def search(request):
     query = request.GET['query']
     sch = post.objects.filter(title__icontains=query)

     return render(request, 'search.html',{'sch':sch})

def login(request): 
     if request.method == 'POST':
          uname = request.POST['username']
          pwd = request.POST['password']
          u = User.objects.get(uname = uname, pwd = pwd)
          if u:
               obj = post.objects.all() 
               return render(request, 'home.html',{'obj':obj})
          else:
               return redirect('/')


     return render(request, 'login.html')

def user(request):
     if request.method == 'POST':
          uname = request.POST['username']
          uemail = request.POST['email']
          pwd = request.POST['password']
          
          u = User(uname=uname,uemail=uemail,pwd=pwd)
          u.save()
          return redirect('/')

     return render(request, 'user.html')