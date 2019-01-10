from django import forms
from django.conf import settings
from django.contrib import admin
from django.forms.widgets import Textarea
from mptt.admin import DraggableMPTTAdmin

from cms import models

class PageForm(forms.ModelForm):
    class Meta:
        model = models.Page
        fields = [
            'title', 'slug', 'author', 'body', 'description', 'featured_image',
            'blog_entry', 'pinned'
        ]

        if 'tinymce' in settings.INSTALLED_APPS:
            from tinymce.widgets import TinyMCE

            widgets = {
                'body': TinyMCE(attrs={'cols': 80, 'rows': 30}),
                'description': Textarea(attrs={'cols': 80, 'rows': 2})
            }


class PageAdmin(admin.ModelAdmin):
    form = PageForm
    list_display = ('title', 'slug', 'blog_entry')
    list_filter = ('blog_entry', )
    readonly_fields = ('date_created', 'last_updated')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(models.Page, PageAdmin)
admin.site.register(models.MenuItem, DraggableMPTTAdmin)
