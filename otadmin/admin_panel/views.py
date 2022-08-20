from django.shortcuts import render
from  django.http import HttpResponse
from django.template import loader
from .models import otData
# /Create your views here. show hello world as text


def index(request):
    template= loader.get_template('dashboard.html')

    return HttpResponse(template.render())

def logData(request):
    queryData = otData.objects.all().values()
    template = loader.get_template('dashboard.html')
    output = ''
    for data in queryData:
        output+=str(data['sno'])+data['dataStream']+' <br> '
    context = {
            'output':output
            }
    return HttpResponse(template.render(context,request))

