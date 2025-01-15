from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpRequest
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import FeedingLogForm
from .models import FeedingLog


# Create your views here.
def home(request: HttpRequest):
    return render(request, "app/home.html")


class FeedingLogCreateView(SuccessMessageMixin, CreateView):
    model = FeedingLog
    form_class = FeedingLogForm
    template_name = "app/home.html"
    success_url = reverse_lazy("home")
    success_message = "Feeding log created"
