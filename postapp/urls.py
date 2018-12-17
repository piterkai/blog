from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^page/(\d+)$', views.index),
    url(r'^post/(\d+)$', views.index_detail),
    url(r'^category/(\d+)$', views.index_category),
    url(r'^archive/(\d+)/(\d+)$', views.index_archive),
    url(r'^archive/$', views.index_archive),
]