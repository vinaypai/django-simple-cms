"""Sitemaps for CMS pages"""
from django.contrib.sitemaps import Sitemap
from cms.models import Page

class BlogSitemap(Sitemap):
    """Sitemap of blog posts"""
    changefreq = 'weekly'
    priority = 0.5

    def items(self):
        return Page.objects.filter(blog_entry=True).order_by('-id')

    def lastmod(self, obj):  #pylint: disable=no-self-use
        """Last date an article was modified"""
        return obj.last_updated
