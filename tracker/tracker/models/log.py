from django.db import models


class Log(models.Model):
    device = models.ForeignKey("tracker.Device", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    meta = models.JSONField(default=dict)

    class Meta:
        verbose_name = 'Log'
        verbose_name_plural = 'Logs'

    def __str__(self):
        return f"{self.device.user.username} : {self.device}"


__all__ = [
    'Log',
]
