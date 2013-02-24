from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.contrib.syndication.views import Feed
from django.core.exceptions import ObjectDoesNotExist
from django.utils.feedgenerator import Atom1Feed, DefaultFeed
from django.shortcuts import get_object_or_404
from djblets.siteconfig.models import SiteConfiguration

from reviewboard.reviews.models import Group, ReviewRequest


def add_domain(url):
    if not (url.startswith("http://") or url.startswith("https://")):
        siteconfig = SiteConfiguration.objects.get_current()
        url = "%s://%s%s" % (siteconfig.get("site_domain_method"),
                             Site.objects.get_current().domain,
                             url)

    return url


class BaseReviewFeed(Feed):

    def item_author_link(self, item):
        return add_domain(item.submitter.get_absolute_url())

    def item_author_name(self, item):
        return item.submitter.username

    def item_author_email(self, item):
        return item.submitter.email

    def item_pubdate(self, item):
        return item.last_updated

    def item_link(self, obj):
        return add_domain(obj.get_absolute_url())


#RSS Feeds
class RssReviewsFeed(BaseReviewFeed):
    title = "Review Requests"
    link = "/r"
    description = "All pending review requests."

    def items(self):
        return ReviewRequest.objects.public()[:20]


class RssSubmitterReviewsFeed(BaseReviewFeed):

    def get_object(self, request, username=None):
        if not username:
            username = request.user.username

        self.feed_type = Atom1Feed if request.GET.get('type', None) == 'atom'\
            else DefaultFeed

        return get_object_or_404(User, username=username)

    def title(self, submitter):
        return u"Review requests to %s" % submitter

    def link(self, submitter):
        return add_domain(submitter.get_absolute_url())

    def description(self, submitter):
        return u"Pending review requests to %s" % submitter

    def items(self, submitter):
        return (ReviewRequest.objects.to_user(submitter.username) |
                ReviewRequest.objects.from_user(submitter.username)).\
            order_by('-last_updated')[:20]


class RssGroupReviewsFeed(BaseReviewFeed):
    def get_object(self, request, groupname):
        self.feed_type = Atom1Feed if request.GET.get('type', None) == 'atom'\
            else DefaultFeed

        return get_object_or_404(Group, name=groupname)

    def title(self, group):
        return u"Review requests to group %s" % group

    def link(self, group):
        return add_domain(group.get_absolute_url())

    def description(self, group):
        return u"Pending review requests to %s" % group

    def items(self, group):
        return ReviewRequest.objects.to_group(group).\
            order_by('-last_updated')[:20]
