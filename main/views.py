from django.shortcuts import render
from main.models import Item
# Create your views here.

def index(request):
    return render(request, 'index.html')