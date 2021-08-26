from django.shortcuts import render
from blog.models import Post
from .models import Teachers

# Create your views here.

def index(request):
    posts = Post.objects.filter(status = 'published', category='maktabga')[:3]
    teachers=Teachers.objects.filter(status='active')[:4]
    teacherss=Teachers.objects.filter(status='active'). all()
    jami=oliy=bir=ikki=mut=0
    for teach in teacherss:
        if teach.degree =='oliy':
            oliy+=1
        if teach.degree =='birinchi':
            bir+=1
        if teach.degree =='ikkinchi':
            ikki+=1
        if teach.degree =='mutaxasis':
            mut+=1
        jami+=1
    #tposts = Post.objects.filter(status = 'published', category='ta\'limga')[:4]
    return render(request, 'index.html', locals())