from django.shortcuts import render
from django.http import HttpResponse
from stalls.models import Stall
from django.template import loader
from django.template import RequestContext


def showListStalls(request):
    stalls_list = []
    for stall in Stall.objects.all():
        stalls_list.append(stall.name)
        stalls_list.append(stall.rating)

    return HttpResponse(stalls_list)