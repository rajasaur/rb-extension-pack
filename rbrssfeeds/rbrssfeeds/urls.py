from django.conf.urls.defaults import patterns, url

from rbrssfeeds.feeds import RssSubmitterReviewsFeed, RssReviewsFeed

urlpatterns = patterns('',
    url(r'^r/$', RssReviewsFeed(), name="all-feeds"),
    url(r'^feed/$', RssSubmitterReviewsFeed(), name="my-feed"),
    url(r'^feed/(?P<username>[A-Za-z0-9@_\-\.]+)/$',
     RssSubmitterReviewsFeed(), name="submitter-feeds"),
)
