from django.db import models


# Create your models here.


class Superhero(models.Model):
    
    nickname= models.CharField(max_length=200,null=True)
    realname=models.CharField(max_length=200, null=True)
    origin_desription=models.CharField(max_length=1000)
    superpowers=models.CharField(max_length=1000,null=True)
    catch_phrase=models.CharField(max_length=300,null=True)
    profile_pic= models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.nickname     
