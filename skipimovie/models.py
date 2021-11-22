from django.db import models

# from skipimovie import settings
# from skipimovie.views import home

class Movie(models.Model):
    id = models.IntegerField(default=1,primary_key=True)
    movie_name=models.CharField(max_length=50)
    movie_year=models.IntegerField(default=0)
    movie_img=models.ImageField(upload_to='images')
    body_img = models.ImageField(upload_to='images')

    def __str__(self):
        return self.movie_name

class browseMovie(models.Model):
    bid = models.IntegerField(default=1,primary_key=True)
    bmovie_name=models.CharField(max_length=50)
    bmovie_year=models.IntegerField(default=0)
    bmovie_img=models.ImageField(upload_to='images/bimg')
    bbody_img = models.ImageField(upload_to='images/bimg')

    def __str__(self):
        return self.bmovie_name

class Contact(models.Model):
    msg_id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=20,default="")
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50,default="")
    number=models.CharField(max_length=10,default="")
    desc=models.CharField(max_length=50,default="")

    def __str__(self):
        return self.name



