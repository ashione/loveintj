from django.shortcuts import render,render_to_response
from django.template import Template,Context,RequestContext
# Create your views here.
def login(request):
    return render_to_response('login.html')
   # return render_to_response('base.html')
    #return render('hello')

def index(request):
    return render_to_response('index.html',RequestContext(request))
