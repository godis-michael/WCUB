from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views import generic

from catalogue.models import Bancnote


def index(request):
    bons = Bancnote.objects.all().order_by('par')
    return render(request, 'catalogue/index.html', {'bons': bons})

def image(request):
    bons = Bancnote()
    variables = RequestContext(request, {
        'bons': bons
    })
    return render_to_response('catalogue/bon_detail.html', variables)