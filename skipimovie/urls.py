
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from . import views, settings
from django.conf.urls.static import static
from .models import Movie

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home.html'),
    # path('downloadpage',views.downloadpage,name='downloadpage.html'),
    path('downloadpage/<int:id>',views.downloadpage,name='downloadpage.html'),
    path('bdownloadpage/<int:bid>',views.bdownloadpage,name='bdownloadpage.html'),
    path('browsemovies',views.browsemovies,name='browsemovies.html'),
    path('contactus',views.contactus,name='contactus.html'),
    # path('mylist',views.mylist,name='mylist.html'),
    path('searchpage',views.searchpage,name='searchpage.html'),
    path('searchpageseries',views.searchpageseries,name='searchpage.html'),
    path('login',views.login,name='login.html'),
    path('signup',views.signup,name='signup.html')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
