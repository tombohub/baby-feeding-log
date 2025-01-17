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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        last_log = FeedingLog.last_submitted_log()
        if last_log:
            self.fields["date"].initial = last_log.date
            self.fields["time"].initial = last_log.time
            self.fields["amount_ml"].initial = last_log.amount_ml
