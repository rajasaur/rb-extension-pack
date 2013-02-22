from django import forms
from djblets.extensions.forms import SettingsForm
from rbcustomreports.models import CustomReports
from rbcustomreports.views import reports


class CustomReportsSettingsForm(SettingsForm):
    selected_reports = forms.MultipleChoiceField(
        choices=[(name, reports[name]['title']) for name in reports])

    def __init__(self, *args, **kwargs):
        super(CustomReportsSettingsForm, self).__init__(*args, **kwargs)
        self.initial['selected_reports'] = \
            [str(val) for val in self.extension.settings['selected_reports']]
