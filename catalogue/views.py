from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, render_to_response
from django.template import RequestContext

from catalogue.models import Bancnote


def index(request):
    bons_list = Bancnote.objects.all().order_by('par')
    page = request.GET.get('page', 1)
    paginator = Paginator(bons_list, 20)
    try:
        bons = paginator.page(page)
    except PageNotAnInteger:
        bons = paginator.page(1)
    except EmptyPage:
        bons = paginator.page(paginator.num_pages)

    index = bons.number - 1
    max_index = len(paginator.page_range)
    start_index = index - 5 if index >= 5 else 0
    end_index = index + 5 if index <= max_index - 5 else max_index
    page_range = paginator.page_range[start_index:end_index]
    return render(request, 'catalogue/index.html', {'bons': bons, 'page_range': page_range})


def image(request):
    bons = Bancnote()
    variables = RequestContext(request, {
        'bons': bons
    })
    return render_to_response('catalogue/bon_detail.html', variables)
