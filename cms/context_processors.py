from django.conf import settings

from cms.models import MenuItem, Page


def navigation(request):
    ctx = {
        'BASE_URL': settings.BASE_URL

    }
    try:
        ctx['main_menu'] = MenuItem.objects.get(label='main')
    except MenuItem.DoesNotExist:
        ctx['main_menu'] = []

    try:
        ctx['footer_menu'] = MenuItem.objects.get(
            label='footer').get_descendants()
    except MenuItem.DoesNotExist:
        ctx['footer_menu'] = []

    try:
        ctx['footer_page'] = Page.objects.get(slug='footer-text')
    except Page.DoesNotExist:
        ctx['footer_page'] = {}

    return ctx
