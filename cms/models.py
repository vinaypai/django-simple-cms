"""Models for CMS pages and navigation menus"""
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Page(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    body = models.TextField()
    description = models.TextField()
    blog_entry = models.BooleanField(default=False)
    pinned = models.BooleanField(default=False)

    featured_image = models.ImageField(
        upload_to='pages/%Y/%m/',
        height_field='featured_image_height',
        width_field='featured_image_width',
        blank=True
    )
    featured_image_height = models.IntegerField(default=0)
    featured_image_width = models.IntegerField(default=0)

    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('cms:page', kwargs={'slug': self.slug})


class MenuItem(MPTTModel):
    label = models.CharField(max_length=30)
    page = models.ForeignKey(Page, on_delete=models.CASCADE, blank=True, null=True)
    link = models.CharField(max_length=100, blank=True, null=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def href(self):
        if self.link:
            return self.link
        elif self.page:
            return self.page.get_absolute_url()
        else:
            return '#'

    def __str__(self):
        return self.label
