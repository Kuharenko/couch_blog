"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
import app.views as views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.test, name='index'),
    url(r'^delete/(?P<post_id>[0-z]+)$', views.remove_post, name="delete"),
url(r'^edit/(?P<post_id>[0-z]+)$', views.post_edit, name="post_edit"),
]