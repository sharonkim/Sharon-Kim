from django.conf.urls import url
import . from views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$', views.process),
    url(r'^success$', views.success),
    url(r'^email/destroy/(?P<id>\d+)$', views.destroy)
]
