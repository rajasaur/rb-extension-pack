# Feeds extension for Review Board.
from django.conf import settings
from django.conf.urls.defaults import patterns, include
from django.http import HttpRequest
from reviewboard.extensions.base import Extension
from reviewboard.extensions.hooks import DashboardHook, URLHook


class MyDashboardHook(DashboardHook):

    def __getattribute__(self, name):
        """ Get Attribute from module
        
        At this point, Reviewboard extensions dont provide a way to get 
        Request object during every page load. The Dashboard hook gets
        its entries when its loaded and uses it for all pages. This
        method uses a (ugly) hack to get the stacktrace from the current 
        page and get the request object(and hence the user object) so I
        can do user specific things. This will change in the future when
        RB provides per-page hooks (as in NavigationBarHook)
        """
        if name == 'entries':
            import sys
            f = sys._getframe()
            username = None
            while f:
                request = f.f_locals.get('request')
                if isinstance(request, HttpRequest):
                    username = request.user.username
                    break
                f = f.f_back

            site_root = settings.SITE_ROOT
            entries = [
                {
                    'label': 'My Feeds',
                    'url': '#',
                    'subitems': [
                        {
                            'label': 'RSS',
                            'url': "%sfeeds/feed/%s" % (site_root, username)
                        },
                        {
                            'label': 'Atom 1',
                            'url': "%sfeeds/feed/%s?type=atom" % (site_root,
                                                                  username)
                        }
                    ]
                },
                {
                    'label': 'All Review Feeds',
                    'url': "%sfeeds/r/" % (site_root,)
                }
            ]
            return entries
        else:
            return DashboardHook.__getattribute__(self, name)


class RSSExtension(Extension):
    is_configurable = False

    def __init__(self, *args, **kwargs):
        super(RSSExtension, self).__init__(*args, **kwargs)

        self.url_hook = URLHook(self, patterns('',
                                (r'^feeds/', include('rbrssfeeds.urls'))))
        self.dashboard_hook = MyDashboardHook(self)
