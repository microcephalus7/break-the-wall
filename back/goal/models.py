from django.db import models
from django.utils import timezone


class Goal(models.Model):
    pubDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)

    title = models.TextField(max_length=50)
    description = models.TextField(max_length=200, null=True)
    status = ["not yet", "doing", "done", "next time"]

    startDate = models.DateTimeField(blank=True)
    endDate = models.DateTimeField(blank=True)
