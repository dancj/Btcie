from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("This is an awesome portfolio history tracker");

def detail(request, tx_id):
    return HttpResponse("You're looking at transaction id %s." % tx_id)

def portfolio(request):
    return HttpResponse("This is the current portfolio state");
