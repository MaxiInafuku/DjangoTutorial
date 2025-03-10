from django.shortcuts import render, redirect
from django.http import HttpResponse #allows to use html code.
from django.contrib.auth.models import User, auth
#messages is used to send a response back.
from django.contrib import messages
from .models import Feature
from .models import Secret


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

    feature4 = Feature()
    feature4.id = 3
    feature4.name = 'Versatility'
    feature4.details = 'Improvise. Adapt. Overcome.'

    #These two lines show the features in the website with our 'manual database'.
    #otherFeatures = [feature2, feature3, feature4]
    #return render(request, 'index.html', {'feature1':feature1, 'otherFeatures':otherFeatures})

    #This uses the database store in db.sqlite3 where data can be uploaded directly from the admin page.
    secrets = Secret.objects.all
    return render(request, 'index.html', {'feature1':feature1, 'otherFeatures':secrets}) 

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        passwordRepetition = request.POST['passwordRepetition']

        if password == passwordRepetition:
            #checks if the email already exists.
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already registered')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'User already registered')
                return redirect('register')
            else:
                user = User.objects.create_user(username = username, email=email, password=password)
                user.save() 
                return redirect('login')
        
        else:
            messages.info(request, "Password doesn't match")
            return redirect('register')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            redirect('login')
    else:
        return render(request, 'login.html')

    return render(request, 'login.html')