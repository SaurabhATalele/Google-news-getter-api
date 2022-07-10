import json
from django.http import HttpResponse
from django.shortcuts import render
from . import pygooglenews as pgn

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

