from django.urls import path, include

from django.contrib import admin
from django.views.generic import TemplateView
from django.views.decorators.cache import cache_page
from hello.views import responseAPI
admin.autodiscover()

import hello.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", hello.views.index, name="index"),
    path("db/", hello.views.db, name="db"),
    path('chatmessage/', cache_page(60 * 15)(responseAPI.as_view())),
    path('globot/', TemplateView.as_view(template_name='test.html')),
    path("admin/", admin.site.urls),
]
