from django.shortcuts import render
from django.http import HttpResponse
import random
import string


def home(request):
    return render(request, 'generator/home.html')

def password(request):

    characters = string.ascii_lowercase
    if request.GET.get('uppercase'):
        characters += string.ascii_uppercase

    if request.GET.get('numbers'):
        characters += string.digits

    if request.GET.get('special'):
        characters += string.punctuation

    length = int(request.GET.get('length', 12)) if 6 <= int(request.GET.get('length')) <= 14 else 12
    thepassword = ''

    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})

def about(request):
    return render(request, 'generator/about.html')