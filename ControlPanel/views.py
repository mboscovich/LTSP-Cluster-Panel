from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    response = "Este es el HTTP Request: %s" % (request)
    return HttpResponse(response)