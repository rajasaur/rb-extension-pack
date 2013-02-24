# rbbroadcastmessage Extension for Review Board.
from django.conf import settings
from django.conf.urls.defaults import patterns, include
from reviewboard.extensions.base import Extension
from reviewboard.extensions.hooks import TemplateHook


class BroadcastMessageExtension(Extension):
    is_configurable = True

    def __init__(self, *args, **kwargs):
        super(BroadcastMessageExtension, self).__init__(*args, **kwargs)

        self.template_hook = TemplateHook(self, 'base-after-navbar',
                                          'rbbroadcastmessage/message.html')
