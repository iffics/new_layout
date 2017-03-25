"""new_layout URL Configuration

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
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from. import views
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    home,
    register,
    logout_user,
    login_user,
    srv,
    s_detail,
    single_shop,
    edit_data,
    re_form,
    revs,
    ser,
    delete_post,


)


app_name = 'my_crs'

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',views.home, name='home'),
    url(r'^register/',register, name='reg'),
    url(r'^logout/',logout_user, name='logout'),
    url(r'^login/',login_user, name='login'),
    url(r'^reg_shop/',srv, name='simple'),
    url(r'^shops/$',s_detail, name='s_detail'),
    url(r'^shop/(?P<id>\d+)/$',single_shop, name='one'),
    url(r'^(?P<id>\d+)/edit/$',edit_data, name='e'),
    url(r'^shop(?P<id>\d+)/del/$',delete_post, name='d'),

    url(r'^add_reviews/$',re_form, name='rform'),
    url(r'^reviews/',revs, name='revs'),
    # url(r'^see/',ser, name='see'),




    #url(r'^(?P<pk>[0-9]+)/',views.single_shop, name='s_detail'),

    #url(r'^shops/',views.shops, name='shops'),
    #url(r'^reviews/',views.rev, name='rev'),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)