# django-simple-cms
A super simple CMS for Django that lets you create pages and blog posts. This app lets you create and manage navigation menus, simple pages like your site's About Us page, and create blog posts. You can edit the raw HTML or optionally use [TinyMCE Lite](https://pypi.org/project/django-tinymce4-lite/) for WYSIWIG editing.

This app is only intended for simple uses by trusted users, and allows you to insert content directly into pages including script tags.

## Requirements
* `django` >= 1.11
* `django-mptt` >= 0.9
* `pillow` >= 2.1
* `django-tinymce4-lite` >= 1.6 (optional, for WYSIWIG editing)

## Quick Start
Install `django-simple-cms`
```
pip install django-simple-cms
```
Add `cms` to `INSTALLED_APPS` in your project's `settings.py`.

```python
INSTALLED_APPS = (
    ...
     'cms',
    ...
)
```

Run migrations in your project to create the models for the CMS app.

```
./manage.py migrate cms
```

If you want WYSIWIG editing, also follow the [installation guide](https://pypi.org/project/django-tinymce4-lite/#quick-start) for `django-tinymce4-lite`.
