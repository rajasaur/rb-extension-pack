from django import template
from djblets.util.decorators import basictag

from reviewboard.extensions.base import get_extension_manager


register = template.Library()


@register.assignment_tag(takes_context=True)
def broadcast_message(context):
    from rbbroadcastmessage.extension import BroadcastMessageExtension
    extension_manager = get_extension_manager()
    extension = extension_manager.get_enabled_extension(
        BroadcastMessageExtension.id)
    if extension.settings.has_key('broadcast_message'):
        return extension.settings['broadcast_message']
    else:
        return ""
