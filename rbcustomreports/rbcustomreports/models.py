from django.db import models
from rbcustomreports.views import reports


class CustomReports(models.Model):
    """
    Add reports that you need to be shown in dashboard.
    """
    selected_reports = models.CharField("selected reports", max_length=128)
