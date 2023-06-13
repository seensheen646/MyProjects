from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import contact,profile
from django.contrib.auth.models import User


def index(request):
    context={}
    if request.method == "POST":
        name = request.POST.get("name")
        em = request.POST.get("email")
        sub = request.POST.get("subject")
        msz = request.POST.get("message")
        obj = contact(name=name,email=em,subject=sub,message=msz)
        obj.save()
        context['message']=(f"Dear {name},Thanks for your feedback!")
    
    return render(request,'index.html',context)

    # return render(request, 'index.html')
def register(request):
    context = {}
    if request.method == "POST":
        #fetch data from html form
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("pass")
        contact = request.POST.get("number")
        try:
          #save data to both table
          usr = User.objects.create_user(email, email,password)
          usr.first_name = name
          usr.save()
          Profile = profile(user =usr, contact_number=contact)
          Profile.save()
          context['status'] = f"Dear {name},you are registered successfully !"

        except:
              context['error'] = f"User with this email already exist!" 

    return render(request,'register.html',context)

def login(request):
    return render(request,'login.html')
def about(request):
    return render(request,'about.html')

def blog(request):
    return render(request,'blog.html')
def menu(request):
    return render(request,'menu.html')
def booking(request):
    return render(request,'booking.html')
def feature(request):
    return render(request,'feature.html')
def team(request):
    return render(request,'team.html')
def contact_us(request):
    context={}
    if request.method == "POST":
        name = request.POST.get("name")
        em = request.POST.get("email")
        sub = request.POST.get("subject")
        msz = request.POST.get("message")
        obj = contact(name=name,email=em,subject=sub,message=msz)
        obj.save()
        context['message']=(f"Dear {name},Thanks for your time!")
    
    return render(request,'contact_us.html',context)

def single(request):
    return render(request,'single.html')
