from django.conf.urls.defaults import patterns, url

from rbbroadcastmessage.extension import BroadcastMessageExtension
from rbbroadcastmessage.forms import BroadcastMessageSettingsForm


urlpatterns = patterns('',
                       (r'^$',
                        'reviewboard.extensions.views.configure_extension',
                        {
                            'ext_class': BroadcastMessageExtension,
                            'form_class': BroadcastMessageSettingsForm
                        })
                       )
