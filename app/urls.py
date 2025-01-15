from django.urls import path

from . import views

urlpatterns = [path("", views.FeedingLogCreateView.as_view(), name="home")]
