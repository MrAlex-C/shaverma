from django.shortcuts import render
from django.http import HttpResponse
from stalls.models import Stall
from django.template import loader
from django.template import RequestContext


def showListStalls(request):
    stalls_list = []
    for stall in Stall.objects.all():
        stalls_list.append(stall)

    template = loader.get_template('stalls.list_stalls')
    context = RequestContext(request, {
        'stalls_list': stalls_list,
    })

    return HttpResponse(template.render(context))