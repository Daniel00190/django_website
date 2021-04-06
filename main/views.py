from django.shortcuts import render
from django.http import HttpResponse

from .models import Post, Other_Post , About_Name

# Create your views here.
def main(request):
    about = About_Name.objects.all()
    posts = Post.objects.all()
    poststwo = Other_Post.objects.all()

    
    return render(request, 'main/home.html', {'posts':posts , 'poststwo': poststwo , 'about': about})
     
