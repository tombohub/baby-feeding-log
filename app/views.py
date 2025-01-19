from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpRequest
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView

from .forms import FeedingLogForm
from .models import FeedingLog


class FeedingLogCreateView(SuccessMessageMixin, CreateView):
    model = FeedingLog
    form_class = FeedingLogForm
    template_name = "app/home.html"
    success_url = reverse_lazy("home")
    success_message = "Feeding log created. Time: %(time)s"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_ml_today"] = FeedingLog.total_ml_today()
        context["today_date"] = timezone.now().date()
        context["last_submitted_log"] = FeedingLog.last_submitted_log
        return context
