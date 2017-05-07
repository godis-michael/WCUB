
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from catalogue.forms import SubscriberForm
from .models import Bancnote
from .filters import BancnoteFilter
from el_pagination.decorators import page_template


@page_template('catalogue/includes/bon_list.html')  # just add this decorator
def bons_list(request, template='catalogue/index.html', extra_context=None):
    bons = Bancnote.objects.all().order_by('par')
    bons_filter = BancnoteFilter(request.GET, queryset=bons)

    context = {
        'bons': bons_filter,
    }
    if extra_context is not None:
        context.update(extra_context)
    return render(request, template, context)


def image(request):
    bons = Bancnote()
    variables = RequestContext(request, {
        'bons': bons
    })
    return render_to_response('catalogue/bon_detail.html', variables)


def feedback(request):
    return render(request, 'catalogue/feedback.html')


def subscribe_us(request):
    if request.method == "POST":
        subscribe_form = SubscriberForm(request.POST)
        if subscribe_form.is_valid():
            subscribe_form.save(commit=True)
            subscribe_form.save()
    else:
        subscribe_form = SubscriberForm()
    return redirect(request.META['HTTP_REFERER'])

