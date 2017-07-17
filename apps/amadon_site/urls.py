from django.conf.urls import url
from views import index, checkout, reset

urlpatterns = [
    url(r'^$', index),
    url(r'^checkout$', checkout),
    url(r'^reset$', reset)
]