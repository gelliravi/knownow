from django.conf.urls import patterns, url

from graphsocial import views

urlpatterns = patterns('',
    # ex: /graphsocial/
    url(r'^$', views.index, name='index'),
    url(r'^create/$', views.createFromScratch, name='createFromScratch'),
)

