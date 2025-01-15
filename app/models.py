from django.db import models

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
