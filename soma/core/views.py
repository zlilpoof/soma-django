from django.shortcuts import render, HttpResponse

# Create your views here.

def soma(request, n1, n2):
    return HttpResponse(f'{n1} + {n2} é: {n1 + n2}')