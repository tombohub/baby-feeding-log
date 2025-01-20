from zoneinfo import ZoneInfo

from django.db import models
from django.utils import timezone

from .utils import get_local_date

# Create your models here.


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class FeedingLog(BaseModel):
    date = models.DateField()
    time = models.TimeField()
    amount_ml = models.SmallIntegerField()

    @classmethod
    def total_ml_today(cls):
        today = get_local_date()
        total = cls.objects.filter(date=today).aggregate(
            total_ml=models.Sum("amount_ml")
        )["total_ml"]
        return total or 0

    @classmethod
    def last_submitted_log(cls):
        """
        Retrieves the most recent FeedingLog entry.

        Returns:
            FeedingLog instance: The latest submitted feeding log.
            None: If no feeding logs are present.
        """
        return cls.objects.order_by("-created_at").first()
