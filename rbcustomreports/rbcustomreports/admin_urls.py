from django.conf.urls.defaults import patterns, include
from rbcustomreports.extension import CustomReportsExtension
from rbcustomreports.forms import CustomReportsSettingsForm

urlpatterns = patterns('',
                       (r'^$',
                        'reviewboard.extensions.views.configure_extension',
                        {
                            'ext_class': CustomReportsExtension,
                            'form_class': CustomReportsSettingsForm
                        })
                       )
