from django.conf.urls import include, url
from . import views
from django.contrib.sitemaps.views import sitemap
from mcdelsi.sitemap import *

sitemaps = {'static': StaticViewSitemap, 'product': ProductSitemap}

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^category/(?P<category>[\w-]+)/$', views.category, name='category'),
    url(r'^product/(?P<product>[\w-]+)/$', views.product, name='product'),
    url(r'^added/(?P<product>[\w-]+)/$', views.added, name='added'),
    url(r'^deleted/(?P<product>[\w-]+)/$', views.deleted, name='deleted'),
    url(r'^cart/$', views.cart, name='cart'),
    url(r'^checkout/$', views.checkout, name='checkout'),
    url(r'^order-confirmation/$', views.order_confirmation, name='order_confirmation'),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap')
]
