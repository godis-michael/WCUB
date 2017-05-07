from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.shortcuts import render

from .models import Bancnote
from .filters import BancnoteFilter

# def search(request):
#     user_list = User.objects.all()
#     user_filter = UserFilter(request.GET, queryset=user_list)
#     return render(request, 'search/user_list.html', {'filter': user_filter})

from el_pagination.decorators import page_template


@page_template('catalogue/includes/bon_list.html')  # just add this decorator
def entry_list(request,
               template='catalogue/catalogue.html', extra_context=None):
    bons_list = Bancnote.objects.all().order_by('par')
    bons_filter = BancnoteFilter(request.GET, queryset=bons_list)

    context = {
        'entry_list': bons_filter,
    }
    if extra_context is not None:
        context.update(extra_context)
    return render(request, template, context)


# def index(request):
#     bons_list = Bancnote.objects.all().order_by('par')
#     bons_filter = BancnoteFilter(request.GET, queryset=bons_list)

    # page = request.GET.get('page', 1)
    # paginator = Paginator(bons_filter, 20)
    # try:
    #     bons = paginator.page(page)
    # except PageNotAnInteger:
    #     bons = paginator.page(1)
    # except EmptyPage:
    #     bons = paginator.page(paginator.num_pages)
    #
    # index = bons.number - 1
    # max_index = len(paginator.page_range)
    # start_index = index - 5 if index >= 5 else 0
    # end_index = index + 5 if index <= max_index - 5 else max_index
    # page_range = paginator.page_range[start_index:end_index]

    # return render(request, 'catalogue/catalogue.html', {'filter': bons_filter,
    #                                                 })


# 'bons': bons,
# 'page_range': page_range


def image(request):
    bons = Bancnote()
    variables = RequestContext(request, {
        'bons': bons
    })
    return render_to_response('catalogue/bon_detail.html', variables)


def feedback(request):
    return render_to_response('catalogue/feedback.html')


def index(request):
    return render_to_response('catalogue/index.html')