from django.db import models

class DisasterReport(models.Model):
    TYPES_CHOICES = [
        ('Earthquake', 'Earthquake'),
        ('Flood', 'Flood'),
        ('Hurricane', 'Hurricane'),
        ('Wildfire', 'Wildfire'),
        ('Tornado', 'Tornado'),
        ('Other', 'Other'),
    ]

    severity_choices = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    type = models.CharField(max_length=20, choices=TYPES_CHOICES)
    severity = models.CharField(max_length=10, choices=severity_choices)
    description = models.TextField()
    reported_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='reports/images/', null=True, blank=True)
