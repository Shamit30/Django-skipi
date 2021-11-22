
from django.contrib import messages 
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.http.response import HttpResponseRedirect 
from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse
from .models import Movie,browseMovie,Contact
from django.contrib.auth.models import User 
from django.contrib.auth  import authenticate,  login, logout

from skipimovie import models, settings

def home(request):
    movies=Movie.objects.all()
    # print(movies)
    params={'movie':movies}
    return render(request,'home.html',params)

def downloadpage(request,id):
    movies=Movie.objects.get(id=id)
    # print(movies)
    # params = {'movie': movies, 'id': id}
    return render(request,'downloadpage.html',{'data':movies})

def searchpage(request):
    query=request.GET['query']
    # if query!=movie_name:
    #     return redirect('not found')
    # print(query)
    data=Movie.objects.filter(movie_name=query)
    return render(request,'searchpage.html',{'data':data})

def searchpageseries(request):
    queryweb=request.GET['queryweb']
    dataweb=browseMovie.objects.filter(bmovie_name=queryweb)
    return render(request,'searchpage.html',{'dataweb':dataweb})


def browsemovies(request):
    # query=request.GET['query']
    browsemovies=browseMovie.objects.all()
    # print(movies)
    params={'bmovie':browsemovies}
    # dataseries=browseMovie.objects.filter(bmovie_name=query)

    return render(request,'browsemovies.html',params)

def bdownloadpage(request,bid):
    browsemovies=browseMovie.objects.get(bid=bid)
    return render(request,'bdownloadpage.html',{'bdata':browsemovies})


def signup(request):
    if request.method=="POST":
        username=request.POST.get('username')
        fname = request.POST.get('fname')
        Email=request.POST.get('Email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')


        if len(username) > 10:
            messages.error(request,"Username must be in 10 character")
            return redirect('/signup')

        if not username.isalnum():
            messages.error(request,'username must be alphanumeric')
            return redirect('/signup')

        if password1 != password2:
            messages.error(request,'password should be same')
            return redirect('/signup')
        

        myuser = User.objects.create_user(username,Email,password1)
        myuser.save()
        messages.success(request,"your account has been successfully created")
        return redirect('/')
    
    return render(request,'signup.html')
    # else:
    #     return HttpResponse('not-found')

def login(request):
    if request.method=="POST":
        loginusername = request.POST.get('loginusername')
        loginpassword = request.POST.get('loginpassword')

        user=authenticate(username=loginusername,password=loginpassword)
        if user is not None:
            messages.success(request,'succesfully logedin')
            return redirect('/')
        else:
            messages.error(request,'Invalid credentials')
            return redirect('/')

    return render(request,'login.html')

def logout(request):
    logout(request)
    return redirect('/')

def contactus(request):
    if request.method=="POST":
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        number=request.POST.get('number','')
        desc=request.POST.get('desc','')
        contactus=Contact(name=name,email=email,number=number,desc=desc)
        # print(name)
        contactus.save()
    return render(request,'contactus.html')

# def mylist(request,id):
#     movie_to_save=get_object_or_404(Movie,movie_id=id)
#     if Movie.objects.filter(user=request.user,movie_id=id).exists():
#         messages.add_message(request,messages.ERROR,"you have already in your list")
#         return HttpResponse("/")
#     user_list,created=mylist.objects.get_or_created(user=request.user)
#     user_list.movie.add(movie_to_save)
#     messages.add_message(request,messages.success,"succesfuly added")
#     return render(request,"mylist.html")

        


   