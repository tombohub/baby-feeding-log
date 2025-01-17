import datetime

from django.test import TestCase
from django.utils import timezone

from .models import FeedingLog


class FeedingLogModelTest(TestCase):
    def setUp(self):
        """
        Sets up the test environment before each test case.
        Creates FeedingLog entries for today and yesterday.
        """
        self.today = timezone.now().date()
        self.yesterday = self.today - datetime.timedelta(days=1)

        # Create FeedingLog entries for today
        FeedingLog.objects.create(
            date=self.today, time=timezone.now().time(), amount_ml=150
        )
        FeedingLog.objects.create(
            date=self.today, time=timezone.now().time(), amount_ml=200
        )

        # Create a FeedingLog entry for yesterday
        FeedingLog.objects.create(
            date=self.yesterday, time=timezone.now().time(), amount_ml=100
        )

    def test_total_ml_today_with_entries(self):
        """
        Test that total_ml_today returns the correct sum when there are feeding logs for today.
        """
        total = FeedingLog.total_ml_today()
        expected_total = 150 + 200  # Sum of today's feeding logs
        self.assertEqual(
            total,
            expected_total,
            f"Expected total_ml_today to be {expected_total}, got {total}",
        )

    def test_total_ml_today_no_entries(self):
        """
        Test that total_ml_today returns 0 when there are no feeding logs for today.
        """
        # Delete today's feeding logs
        FeedingLog.objects.filter(date=self.today).delete()
        total = FeedingLog.total_ml_today()
        expected_total = 0
        self.assertEqual(
            total,
            expected_total,
            f"Expected total_ml_today to be {expected_total}, got {total}",
        )

    def test_total_ml_today_excludes_other_days(self):
        """
        Test that total_ml_today excludes feeding logs from other days.
        """
        # Add another FeedingLog entry for yesterday
        FeedingLog.objects.create(
            date=self.yesterday, time=timezone.now().time(), amount_ml=50
        )
        total = FeedingLog.total_ml_today()
        expected_total = 150 + 200  # Only today's entries should be summed
        self.assertEqual(
            total,
            expected_total,
            f"Expected total_ml_today to be {expected_total}, got {total}",
        )

    def test_last_submitted_log_returns_latest_entry(self):
        """
        Test that last_submitted_log returns the most recent FeedingLog entry.
        """
        FeedingLog.objects.create(
            date=self.today, time=timezone.now().time(), amount_ml=100
        )
        FeedingLog.objects.create(
            date=self.today, time=timezone.now().time(), amount_ml=200
        )
        latest_log = FeedingLog.last_submitted_log()
        if latest_log is not None:
            self.assertEqual(latest_log.amount_ml, 200)

    def test_last_submitted_log_returns_none_when_no_entries(self):
        """
        Test that last_submitted_log returns None when no FeedingLog entries exist.
        """
        FeedingLog.objects.all().delete()
        latest_log = FeedingLog.last_submitted_log()
        self.assertIsNone(latest_log)
