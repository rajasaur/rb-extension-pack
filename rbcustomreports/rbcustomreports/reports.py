from django.db.models import Q

from reviewboard.reviews.models import ReviewRequest, Review
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
