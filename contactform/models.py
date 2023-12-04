from django.db import models


class ContactUs(models.Model):
    name = models.CharField(max_length=80, null=True, blank=True)
    email = models.CharField(max_length=80, null=True, blank=True)
    phone = models.CharField(max_length=80, null=True, blank=True)
    department = models.CharField(max_length=80, null=True, blank=True)
    title = models.CharField(max_length=80, null=True, blank=True)
    body = models.TextField(max_length=80, null=True, blank=True)
    track_code = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    checked = models.BooleanField(default=False)
