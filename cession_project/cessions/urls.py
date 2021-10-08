from django.conf import urls
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.listing, name='listing'),
    url(r'^(?P<book_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^search/$', views.search, name='search'),
]
