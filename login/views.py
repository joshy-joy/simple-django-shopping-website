from django.shortcuts import render
from .models import User
# Create your views here.
def login(request):
    if request.method == 'POST':
        
