from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from el_pagination.decorators import page_template

from .decorators import check_recaptcha
from .filters import BancnoteFilter
from .forms import SubscriberForm, FeedbackForm
from .models import Bancnote, Article


def index(request):
    news = Article.objects.all().order_by('-published_date')
    return render(request, 'catalogue/index.html', {'news': news})


@page_template('catalogue/includes/bon_list.html')  # just add this decorator
def bons_list(request, template='catalogue/catalogue.html', extra_context=None):
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


@check_recaptcha
def feedback(request):
    if request.method == 'GET':
        form = FeedbackForm()
    else:
        form = FeedbackForm(request.POST)
        if form.is_valid() and request.recaptcha_is_valid:
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            # msg = EmailMultiAlternatives(subject, message, from_email, [receipient])
            # respone = msg.send()
            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "catalogue/feedback.html", {'form': form})


def feedback_success(request):
    return HttpResponse('Success! Thank you for your message.')


def subscribe_us(request):
    if request.method == "POST":
        subscribe_form = SubscriberForm(request.POST)
        if subscribe_form.is_valid():
            subscribe_form.save(commit=True)
            subscribe_form.save()
    else:
        subscribe_form = SubscriberForm()
    return redirect(request.META['HTTP_REFERER'])

