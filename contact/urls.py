"""contact URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$','default.views.log'),
    url(r'^reg/$','default.views.reg'),
    url(r'^reging/$','default.views.reging'),
    url(r'^getlist/$','default.views.getlist'),
    url(r'^add/$','default.views.addlist'),
    url(r'^update/$','default.views.updatelist'),
    url(r'^del/$','default.views.dellist'),
    url(r'^loging/$','default.views.loging'),
    url(r'^more/$','default.views.more'),
    url(r'^find/$','default.views.find'),
]
