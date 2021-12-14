from django.db import models


class Tour(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, null=False, blank=False)
    preferred_time = models.CharField(max_length=100)
