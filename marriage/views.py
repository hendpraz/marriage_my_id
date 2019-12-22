from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, you're at the marriage.my.id index")

def tania_dika_index(request):
    return HttpResponse("Index page")

def tania_dika_invitation(request, guest_name):
    return HttpResponse("Hello, %s." % guest_name)