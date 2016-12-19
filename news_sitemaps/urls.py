from django.conf.urls import url

from news_sitemaps import registry
from .views import index, news_sitemap

urlpatterns = [
    url(r'^index\.xml$',
        index,
        {'sitemaps': registry},
        name='news_sitemaps_index'),

    url(r'^(?P<section>.+)\.xml',
        news_sitemap,
        {'sitemaps': registry},
        name='news_sitemaps_sitemap'),
]
