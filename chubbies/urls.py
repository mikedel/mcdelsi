from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^category/(?P<category>[\w-]+)/$', views.category, name='category'),
    url(r'^product/(?P<product>[\w-]+)/$', views.product, name='product'),
    url(r'^added/(?P<product>[\w-]+)/$', views.added, name='added'),
    url(r'^deleted/(?P<product>[\w-]+)/$', views.deleted, name='deleted'),
    url(r'^cart/$', views.cart, name='cart'),
    url(r'^checkout/$', views.checkout, name='checkout'),
    url(r'^order-confirmation/$', views.order_confirmation, name='order_confirmation'),
]
