from django.conf.urls import url
from django.views.generic import DetailView

from catalogue import views
from catalogue.models import Bancnote

urlpatterns = [
    url(r'^$', views.entry_list, name='entry_list'),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Bancnote, template_name='catalogue/bon_detail.html')),
    url(r'^feedback/$', views.feedback, name='feedback'),
]
