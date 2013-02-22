from datetime import datetime, timedelta

from django.http import Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext

from reviewboard.extensions.hooks import DashboardHook

from rbcustomreports.reports import NotClosedWithShipItReport,\
    NotReviewedReport, NotReviewedByMeReport, FilterByRepositoryReport
from rbcustomreports.datagrids import CustomDataGrid

reports = {
    'not_closed_with_shipit': {
        'data_class': NotClosedWithShipItReport,
        'title': 'Not Closed with ShipIt',
    },
    'not_reviewed': {
        'data_class': NotReviewedReport,
        'title': 'Not Reviewed Requests',
    },
    'not_reviewed_by_me': {
        'data_class': NotReviewedByMeReport,
        'title': 'Not Reviewed By Me Requests',
    },
    'filter_by_repo': {
        'data_class': FilterByRepositoryReport,
        'title': 'Filter by Repository'
    }
}


def report(request,
           template_name='reviews/dashboard.html'):
    report_name = request.GET.get('name', None)
    if not report_name:
        raise Http404

    report_title = reports[report_name]['title']
    if not report_title:
        raise Http404

    extra_context = {}
    rb_object = request.GET.get('object', None)
    if rb_object:
        extra_context['rb_object'] = rb_object

    grid = reports[report_name]['data_class'](request, title=report_title,
                                              extra_context=extra_context)
    return grid.render_to_response(template_name, extra_context={
        'sidebar_hooks': DashboardHook.hooks,
    })


def configure(request,
              template_name='rbcustomreports/configure.html'):
    return render_to_response(template_name, RequestContext(request, {
    }))
