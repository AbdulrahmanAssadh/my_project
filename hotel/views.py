
from django.http import HttpResponse
from django.shortcuts import redirect, render
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from hotel.models import *
from datetime import datetime

#oop 
class  hotel:
    def __init__(self,name,location,evaluation,url,price=0):
        self.name=name
        self.price=price
        self.location=location
        self.evaluation=evaluation
        self.url=url
        
        
        

def index(request):
    print(request.user)
    return render(request,'index.html')



def search(request):
    
    if request.method =='POST':
        ss=request.POST.get('ss')
        sb_entire_place=request.POST.get('sb_entire_place')
        group_adults=request.POST.get('group_adults')
        checkin=request.POST.get('checkin')
        checkout=request.POST.get('checkout')
        evaluation=request.POST.get('evaluation')
      
        
        url="https://www.booking.com/searchresults.ar.html?ss={}&sb_entire_place={}&group_adults={}&checkin={}&checkout={}&nflt=class%3D{}".format(ss,sb_entire_place,group_adults,checkin,checkout,evaluation)
        pathDriver="c:/Users\Abdalrahman\Desktop\web_py\my_project\hotel\chromedriver";
        browser = webdriver.Chrome(executable_path=pathDriver);
        browser.get(url)
        soup= BeautifulSoup(browser.page_source,'lxml')
        
        browser.quit()        
        hotel_tag=soup.find_all('div',{'class':'d20f4628d0'})
        
        # hotel_name=soup.find_all('div',{'class':'fcab3ed991 a23c043802'})
        
        hotels=[]
        
        
      
        
        for item in hotel_tag:
            name=item.find('div',{'class':'fcab3ed991 a23c043802'})
            location=item.find('span',{'class':'b4273d69aa'})
            price=item.find('span',{'class':'e729ed5ab6'})
            url=item.find('a',{'class':'fc63351294'})
            evaluation=item.find('div',{'class':'b5cd09854e d10a6220b4'})
            hotels.append(hotel(name=name.text,location=location.text,evaluation=evaluation.text,url=url['href'])) #,price=price.text
         
         
        hotels.sort(reverse=True,key=lambda e:e.evaluation)   
              
        d1 = datetime.strptime(checkin, "%Y-%m-%d")
        d2 = datetime.strptime(checkout, "%Y-%m-%d")
        day=d2-d1
        
    return render(request,'search.html',{'hotels':hotels,'checkin':checkin,'checkout':checkout,'day':day.days,'post':request.POST})





def index_m(request,token):
    
    
    user=DataUser.objects.filter(num2=token)[0]
    print(user)
    if user :
         return render(request,'m/index.html',{'user':user})
    else:
         return HttpResponse('404 this user is not found')
    
    # return render(request,'m/index.html')







def data_m(request):  
    users=DataUser.objects.all()  
    
    return render(request,'m/search.html',{'users':users})



def save_m(request):
     if request.method == 'POST':
            num1=request.POST['num1']
            num2=request.POST['num2']
            name1=request.POST['name1']
            name2=request.POST['name2']
        
            user=DataUser.objects.create(num1=num1,num2=num2,name1=name1,name2=name2)
            user.save()
        
     return  redirect('data_m')  