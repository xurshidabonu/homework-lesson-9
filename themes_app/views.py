from django.shortcuts import render

# Create your views here.

def get_lessons_hammasi():
    with open('lessons.txt','r') as file:
        lessons=file.readlines()
    return lessons

def index(request):
    lessons=get_lessons_hammasi()
    return render(request,'index.html',{'lessons':lessons})




