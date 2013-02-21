from django.db.models import Q

from reviewboard.reviews.models import ReviewRequest, Review
from reviewboard.scmtools.models import Repository
from rbcustomreports.datagrids import CustomDataGrid


class NotClosedWithShipItReport(CustomDataGrid):
    def get_queryset(self, profile):
        queryset = ReviewRequest.objects.filter(Q(public=True) &
                                                Q(status='P') &
                                                Q(shipit_count__gt=0))
        return queryset


class NotReviewedReport(CustomDataGrid):
    def get_queryset(self, profile):
        queryset = ReviewRequest.objects.filter(Q(public=True) &
                                                Q(reviews__isnull=True))
        return queryset


class NotReviewedByMeReport(CustomDataGrid):

    def get_queryset(self, profile):
        queryset = ReviewRequest.objects.filter(Q(public=True) &
                                                Q(status='P') &
                                                ~Q(reviews__user=
                                                   self.request.user))
        return queryset


class FilterByRepositoryReport(CustomDataGrid):

    def get_queryset(self, profile):
        repo_id = self.extra_context['rb_object']
        repo_name = Repository.objects.get(pk=int(repo_id)).name

        self.title = "Filter by Repository - %s" % (repo_name,)

        queryset = ReviewRequest.objects.filter(Q(public=True) &
                                                Q(status='P') &
                                                Q(repository=repo_id) &
                                                (Q(repository__public=1) |
                                                 Q(repository__users__in=[self.request.user]) |
                                                 Q(repository__review_groups__users__in=[self.request.user])))

        return queryset
