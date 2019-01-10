from django.urls import path

from . import views

app_name = 'cms'

urlpatterns = [
    path('blog/', views.blog_index, name='blog_index'),
    path('<slug>/', views.page, name='page'),
]
