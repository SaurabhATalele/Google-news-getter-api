import json
from django.http import HttpResponse
from django.shortcuts import render
from . import pygooglenews as pgn
from . import database as db

# Create your views here.

def Home(request):
    return render(request,'Home.html')

def lang(request,param):

    gn = pgn.GoogleNews(lang=param,country="IN")

    response_data = gn.top_news()
    print(response_data['entries'][0]['title'])
    return HttpResponse(json.dumps(response_data), content_type="application/json")

def top_Head(request,param,topic):

    gn = pgn.GoogleNews(lang=param,country="IN")
    print(topic)
    response_data = gn.topic_headlines(topic)
    print(response_data['entries'][0]['title'])
    return HttpResponse(json.dumps(response_data), content_type="application/json")

def load_login(request):
    return render(request,'Login.html')

def home_login(request):
    pass


def addnews(request):
    return render(request,'AddNews.html')

# Adding the new to the database 
def create_news(request):
    data = db.db
    # sample = {"Ministry": "Prime Minister"}
    # sample = {"name": "zatuji"}
    # data.child("users").child("Morty").update(sample)
    ministry = request.POST['ministries']
    title = request.POST['nametitle']
    desc = request.POST['desc']
    print(ministry)
    # sample = {
    #     'title':title,
    #     "description":desc
    # }
    # data.child('Ministry').child("min1").set(sample)
    a = data.child('Ministry').child("min1").get()
    val = a.val()["description"]
    print(val)



    return render(request,'AddNews.html')
