from django.db import models


class Tour(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, null=False, blank=False)
    preferred_date = models.DateField(null=True)

    PREFERRED_TIME_CHOICES = [
        ('13:30', '13:30'),
        ('15:30', '15:30'),
    ]

    preferred_time = models.CharField(
        max_length=5,
        choices=PREFERRED_TIME_CHOICES,
    )
