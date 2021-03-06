from django import forms
from djblets.extensions.forms import SettingsForm
from rbcustomreports.views import reports


class CustomReportsSettingsForm(SettingsForm):
    selected_reports = forms.MultipleChoiceField(
        choices=[(name, reports[name]['title']) for name in reports])

    def __init__(self, *args, **kwargs):
        super(CustomReportsSettingsForm, self).__init__(*args, **kwargs)
        if self.extension.settings.has_key('selected_reports'):
            self.initial['selected_reports'] = \
                [str(val) for val in self.extension.settings['selected_reports']]
