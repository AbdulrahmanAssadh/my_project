from django.db import models

# Create your models here.


class Hotel (models.Model) :
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    rank= models.IntegerField()
    location= models.CharField(max_length=255)
    
    # def  __str__(self) :
    #     return  self.name
    
    
    
class  DataUser(models.Model):
         id = models.BigAutoField(primary_key=True)
         num1=models.IntegerField()
         num2=models.IntegerField()
         name1=models.CharField(max_length=255)
         name2=models.CharField(max_length=255)
    
