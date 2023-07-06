from django.db import models


class Record(models.Model):
    session = models.ForeignKey("session.Session", on_delete=models.CASCADE)
    user = models.ForeignKey("user.User", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Record'
        verbose_name_plural = 'Records'

    def __str__(self):
        return f"{self.user.username} : {self.session.name} - {self.timestamp}"


__all__ = [
    "Record"
]
