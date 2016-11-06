from django.shortcuts import render
from django.http import HttpResponse
from stalls.models import Stall
from django.template import loader
from django.template import RequestContext


def showListStalls(request):
    stall_name = Stall.name
    stall_main_picture = Stall.main_picture
    stall_description = Stall.description
    stall_reviews_counter = Stall.reviews_counter
    stall_rating = Stall.rating
    stall_address = Stall.address
    stall_name = 'name'
    stall_rating = 15
    template = loader.get_template('stalls/list stalls.html')
    context = RequestContext(request, {
        'stall_name': stall_name,
        'stall_main_picture': stall_main_picture,
        'stall_description': stall_description,
        'stall_reviews_counter': stall_reviews_counter,
        'stall_rating': stall_rating,
        'stall_address': stall_address
    })
    return HttpResponse(template.render(context))