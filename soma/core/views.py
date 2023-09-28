from django.shortcuts import render, HttpResponse

# Create your views here.

def soma(request, n1, n2):
    return HttpResponse(f'{n1} + {n2} é: {n1 + n2}')

def multiplicacao(request, n1, n2):
    return HttpResponse(f'{n1} * {n2} é: {n1 * n2}')

def divisao(request, n1, n2):
    return HttpResponse(f'{n1} / {n2} é: {n1 / n2}')

def subtracao(request, n1, n2):
    return HttpResponse(f'{n1} - {n2} é: {n1 - n2}')