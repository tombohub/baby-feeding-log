from django import forms

from .models import FeedingLog


class FeedingLogForm(forms.ModelForm):
    class Meta:
        model = FeedingLog
        fields = ["date", "time", "amount_ml"]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
            "time": forms.TimeInput(attrs={"type": "time"}),
        }
