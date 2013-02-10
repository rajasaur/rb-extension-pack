from django.conf.urls.defaults import patterns, include


urlpatterns = patterns('',
                       (r'^$', 'rbcustomreports.views.configure')
                       )
