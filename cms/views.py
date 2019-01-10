"CMS views"

from django.conf import settings
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, render

from cms.models import Page


def page(request, slug):
    """Serve a CMS page view"""

    ctx = {}
    page_obj = get_object_or_404(Page, slug=slug)
    ctx['page'] = page_obj
    ctx['BASE_URL'] = settings.BASE_URL

    return render(request, 'cms/page.html', ctx)


def blog_index(request):
    """The index of all blog posts"""

    ctx = {}
    entries = Page.objects.filter(blog_entry=True).order_by(
        '-pinned', '-date_created')
    paginator = Paginator(entries, 10)
    page_num = request.GET.get('page')
    ctx['BASE_URL'] = settings.BASE_URL

    try:
        entries = paginator.page(page_num)
    except PageNotAnInteger:
        entries = paginator.page(1)
    except EmptyPage:
        entries = paginator.page(paginator.num_pages)

    ctx['entries'] = entries

    return render(request, 'cms/blog_index.html', ctx)
