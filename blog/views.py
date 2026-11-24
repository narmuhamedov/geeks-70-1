from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from blog.models import Blog


def blog_mem_detail_view(request, id):
    if request.method == "GET":
        blog_id = get_object_or_404(Blog, id=id)
    return render(request, 'blog_detail.html', {'blog_id': blog_id})


def blog_mem_view(request):
    if request.method == "GET":
        blog = Blog.objects.all().order_by('-id')
    return render(request, 'blog_list.html', {'blog_list': blog})








def hello_world_view(request):
    if request.method == "GET":
        return HttpResponse('Привет это мой первый проект на Django')

def about_me_view(request):
    if request.method == "GET":
        return HttpResponse('Меня зовут Радомир, мне 29 лет, Я Backend Dev')