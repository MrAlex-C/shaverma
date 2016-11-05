from django.shortcuts import render
from django.http import HttpResponse
from stalls.models import Stall
from django.template import loader
from django.template import RequestContext


def showListStalls(request):
    stall_name = Stall.name
    template = loader.get_template('stalls/list stals.html')
    context = RequestContext(request, {
        'stall_name': stall_name,
    })
    return HttpResponse(template.render(context))