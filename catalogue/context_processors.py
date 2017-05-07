from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import timezone

from .forms import SubscriberForm


def SubscribeFormGlobal(request):
    return {'subscribe_form': SubscriberForm()}

# def subscribe_us(request):
#     if request.method == "POST":
#         subscribe_form = SubscriberForm(data=request.POST)
#         if subscribe_form.is_valid():
#             subscribe = subscribe_form.save(commit=False)
#             subscribe.author = request.user
#             subscribe.published_date = timezone.now()
#             subscribe.save()
#         else:
#             subscribe_form = SubscriberForm()
#         return render_to_response(
#             'catalogue/includes/footer.html',
#             {'subscribe_form': subscribe_form},
#             context_instance=RequestContext(request),
#         )
