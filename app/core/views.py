
from django.shortcuts import render
from contact.models import Contactinfo

def index(request):
    return render(request, 'home/index.html')