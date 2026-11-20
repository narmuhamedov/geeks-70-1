from django.shortcuts import render
from django.http import HttpResponse

def hello_world_view(request):
    if request.method == "GET":
        return HttpResponse('Привет это мой первый проект на Django')

def about_me_view(request):
    if request.method == "GET":
        return HttpResponse('Меня зовут Радомир, мне 29 лет, Я Backend Dev')