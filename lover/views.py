from django.shortcuts import render,render_to_response
from django.template import Template,Context
# Create your views here.
def login(request):
    return render_to_response('lover/login.html')
   # return render_to_response('base.html')
    #return render('hello')
