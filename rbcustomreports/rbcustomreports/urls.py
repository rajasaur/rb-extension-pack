from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('rbcustomreports.views',
                       (url(r'^$', 'report', name='report_list')),
                       (url(r'^customreports/$', 'report',
                            name='custom_report')),
                       )
