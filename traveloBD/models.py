from django.db import models

# Create your models here.

class Dist_info(models.Model):
    name= models.CharField(null=False,max_length=120)
    des=models.TextField(null=False,blank=False,default='give the describtion')
    img=models.ImageField(null=True,blank=True,upload_to="img/%y")


    def __str__(self):
        return self.name

class Tour_places(models.Model):
    name = models.CharField(null=False, max_length=120)
    des = models.TextField(null=False, blank=False, default='give the describtion')
    img = models.ImageField(null=True, blank=True, upload_to="img/%y")

    dist_info=models.ForeignKey(Dist_info,null=True,on_delete = models.SET_NULL)

    def __str__(self):
        return self.name


class Gallery_photos(models.Model):
    name=models.CharField(max_length=100)

    img = models.ImageField(null=True, blank=True, upload_to="img/%y")
    def __str__(self):
        return self.name

class PopulerPlaces(models.Model):
    name= models.CharField(null=False,max_length=120)
    des=models.TextField(null=False,blank=False,default='give the describtion')
    img=models.ImageField(null=True,blank=True,upload_to="img/%y")

    def __str__(self):
        return self.name



