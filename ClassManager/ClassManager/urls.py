from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf.urls import include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#from studentmanger.views import post_new
from studentmanger.views import classes_new
from studentmanger.views import classtest
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ClassManager.views.home', name='home'),
    # url(r'^ClassManager/', include('ClassManager.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^clsadd/',classes_new,name='classes_new'),
    url(r'^class/post','studentmanger.classops.addclass',name='addclass'),
    url(r'^clstat/',classtest,name='classtest'),
    #url(r'^post/(?P<pk>[0-9]+)/$', post_detail),
    #url(r'^post/new/$', post_new, name='post_new'),
    #url(r'^classlist'),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += staticfiles_urlpatterns()