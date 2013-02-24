from django import forms
from djblets.extensions.forms import SettingsForm


class BroadcastMessageSettingsForm(SettingsForm):
    widget = forms.Textarea(attrs={'cols': 70, 'rows': 4})
    broadcast_message = forms.CharField(max_length=128,
                                        required=False,
                                        help_text="Enter a broadcast message\
                                        (Only text please and maximum 128\
                                        chars). Clear text to remove existing\
                                        message.",
                                        widget=widget)
