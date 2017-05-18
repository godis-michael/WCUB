from django.conf.urls import url
from django.views.generic import DetailView

from catalogue import views
from .models import Bancnote, Article

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^catalogue/$', views.bons_list, name='catalogue'),
    url(r'^feedback/$', views.feedback, name='feedback'),
    url(r'^subscribe/$', views.subscribe_us, name='subscribe'),
    url(r'^catalogue/(?P<pk>\d+)/$', DetailView.as_view(model=Bancnote, template_name='catalogue/bon_detail.html')),
    url(r'^feedback/success/$', views.feedback_success, name='success'),
    url(r'^news/(?P<pk>\d+)/$', DetailView.as_view(model=Article, template_name='catalogue/article_detailed.html'))
]
