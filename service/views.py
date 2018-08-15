from django.shortcuts import render
from django.http import HttpResponse
from .models import customer
# Create your views here.

def index(request):
    return render(request,'service/index.html')



def submit(request):
    first_name = request.POST["firstname"]
    last_name = request.POST["lastname"]
    country = request.POST["country"]

    cust = customer(first_name=first_name,last_name=last_name,country_name=country)
    cust.save()
    
    return render(request,'service/index.html')
