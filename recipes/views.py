from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return  HttpResponse('''<!DOCTYPE>
    <html>
    <head><title>Olá mundo</title></head>

    <body>
        <h1>Olá mundo</h1>
    </body>

    </html>
    
    
    ''')

def contato(request):
    return  HttpResponse('contato')

def sobre(request):
    return  HttpResponse('sobre')

