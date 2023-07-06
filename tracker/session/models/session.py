from django.db import models
import uuid


class Session(models.Model):
    key = models.UUIDField(
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    instructor = models.ForeignKey("user.User", on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Session'
        verbose_name_plural = 'Sessions'

    def __str__(self):
        return f"{self.name} [{self.key}] {self.start_time}"


__all__ = [
    "Session"
]
