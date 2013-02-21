# Reports extension for Review Board.
from django.db.models import Q
from django.conf import settings
from django.conf.urls.defaults import patterns, include
from django.contrib.auth.models import User
from django.http import HttpRequest
from reviewboard.extensions.base import Extension
from reviewboard.extensions.hooks import DashboardHook, URLHook
from reviewboard.scmtools.models import Repository


class UserBasedDashboardHook(DashboardHook):
    def __init__(self, extension, entries):
        self.main_entries = entries
        super(DashboardHook, self).__init__(extension)

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

            user = User.objects.filter(username=username)
            repositories = Repository.objects.filter(Q(public=1) |
                                                     Q(users__in=user) |
                                                     Q(review_groups__users__in=user))

            if len(repositories) == 0:
                return self.main_entries
            else:
                entries = {
                    'label': 'Filter by Repository',
                    'url': '#',
                }
                subitems = []
                for repo in repositories:
                    subitem = {'label': str(repo.name),
                               'url': settings.SITE_ROOT +
                               "customreports/?name=filter_by_repo&object=" +
                               str(repo.id)
                               }
                    subitems.append(subitem)

                entries['subitems'] = subitems

                cloned_main_entries = self.main_entries[:]
                cloned_main_entries.append(entries)

                return cloned_main_entries
        else:
            return DashboardHook.__getattribute__(self, name)


class CustomReportsExtension(Extension):
    is_configurable = True

    def __init__(self, *args, **kwargs):
        super(CustomReportsExtension, self).__init__(*args, **kwargs)

        self.url_hook = URLHook(self, patterns('',
                                (r'^customreports/',
                                 include('rbcustomreports.urls'))))

        self.dashboard_hook = UserBasedDashboardHook(self, entries=[
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
