from django.shortcuts import render
from django.http import HttpResponse

# MAIN WEB PAGES

def index(request):
    return render(request, 'marriage/main-page/index.html')

# CLIENT WEB PAGES

def tania_dika_index(request):
    return render(request, 'marriage/tania-dika/index.html')

def tania_dika_invitation(request, guest_name):
    return render(request, 'marriage/tania-dika/index.html')