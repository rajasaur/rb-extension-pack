# Reports extension for Review Board.
from django.conf import settings
from django.conf.urls.defaults import patterns, include
from reviewboard.extensions.base import Extension
from reviewboard.extensions.hooks import DashboardHook, URLHook


class CustomReportsExtension(Extension):
    is_configurable = True

    def __init__(self, *args, **kwargs):
        super(CustomReportsExtension, self).__init__(*args, **kwargs)

        self.url_hook = URLHook(self, patterns('',
                                (r'^customreports/',
                                 include('rbcustomreports.urls'))))

        self.dashboard_hook = DashboardHook(self, entries=[
            {
                'label': 'Reports',
                'url': '#',
                'subitems': [
                    {
                        'label': 'Not closed with Shipit',
                        'url': settings.SITE_ROOT +
                        "customreports/?name=not_closed_with_shipit",
                    },
                    {
                        'label': 'Not Reviewed',
                        'url': settings.SITE_ROOT +
                        "customreports/?name=not_reviewed",
                    },
                    {
                        'label': 'Not Reviewed By Me',
                        'url': settings.SITE_ROOT +
                        "customreports/?name=not_reviewed_by_me",
                    }
                ]
            }
        ])
