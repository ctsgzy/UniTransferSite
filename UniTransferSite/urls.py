from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
admin.autodiscover()
# And include this URLpattern...
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'UniTransferSite.views.home', name='home'),
    # url(r'^UniTransferSite/', include('UniTransferSite.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'UniTransferSite.views.defaultpage'),
    url(r'^bootstrap', 'UniTransferSite.views.bootstrap_template'),
    url(r'^login/','ulogin.views.loginView'),
    url(r'^showloginpage/','ulogin.views.showLoginPage'),
    url(r'^logout/','ulogin.views.logoutView'),
    url(r'^regist/','regist.views.registView'),
    url(r'^orderpack/','mypacks.views.orderpackinput'),
    url(r'^orderpacksubmit/','mypacks.views.orderpacksubmit'),
    url(r'^mypacks/','mypacks.views.showmypacks'),
    url(r'^getpacksaj','mypacks.views.getpacksaj'),
    (r'^statics/(?P<path>.*)$','django.views.static.serve',{'document_root': settings.STATIC_ROOT}),
)
