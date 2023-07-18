from django.shortcuts import render
from django.shortcuts import HttpResponse
import random
# Create your views here.
number = random.randint(1,10)
def secret_number(request):
    
  
    return HttpResponse(number)
def welcome(request):
    return HttpResponse("welcome")
#def attempt():

    