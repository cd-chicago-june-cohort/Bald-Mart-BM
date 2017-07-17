from django.conf.urls import url
from views import index, checkout, reset, show_cart

urlpatterns = [
    url(r'^$', index),
    url(r'^checkout$', checkout),
    url(r'^reset$', reset),
    url(r'^show_cart', show_cart)
]