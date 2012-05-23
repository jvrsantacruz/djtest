from django.conf.urls.defaults import *

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
    url('^$', 'djtest.views.index', name='djtest-main'),
    url('^sendnews$', 'djtest.views.sendnews', name='djtest-send'),

    url('^login$', 'django.contrib.auth.views.login', name="djtest-login"),
    url('^logout$', 'django.contrib.auth.views.logout_then_login', name="djtest-logout"),
    url('^register$', 'djtest.views.register', name="djtest-register"),

    url('^pressimg/(?P<pressnewid>\d+)/$', 'djtest.views.pressimg', name='pressimg'),
)
