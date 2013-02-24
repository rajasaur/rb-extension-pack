from django.db import models


class BroadcastMessage(models.Model):
    """
    Store the broadcast message
    """
    broadcast_message = models.CharField("broadcast message",
                                         max_length=128,
                                         blank=True)
