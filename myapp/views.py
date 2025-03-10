from django.shortcuts import render
from django.http import HttpResponse #allows to use html code.
from .models import Feature

# Create your views here.

'''
#This is a dumb example. It is better to have the html templates in a separate directory and call them.
def test(request):
    return HttpResponse('<h1>Hey, Welcome</h1>') 
'''

def test(request):
    context = {
        'name': 'Lu',
        'ID': 274,
        'carrer': 'geology'
    }
    return render(request, 'test.html', context)

def counter(request):
    userText = request.POST['userText']
    wordCount = len(userText.split())
    context = {
        'userText': userText,
        'wordCount': wordCount
        }
    return render(request, 'counter.html', context)

def index(request):
    feature1 = Feature()
    feature1.id = 0
    feature1.name = 'Contact'
    feature1.details = 'Give us a call: 11-1111-1111'

    
    feature2 = Feature()
    feature2.id = 1
    feature2.name = 'Power Training'
    feature2.details = 'Our personal trainers are the very best you can find around.'

    
    feature3 = Feature()
    feature3.id = 2
    feature3.name = 'Dedication'
    feature3.details = 'We expect you to also compromise to always be better.'

    context = {'feature1':feature1, 'feature2':feature2, 'feature3':feature3}

    return render(request, 'index.html', context)
