from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import timezone

from .forms import SubscriberForm


def SubscribeFormGlobal(request):
    return {'subscribe_form': SubscriberForm()}
