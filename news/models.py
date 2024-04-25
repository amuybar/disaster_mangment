from django.db import models

class NewsArticle(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField()
    source = models.CharField(max_length=200)
    published_at = models.DateTimeField()

    def __str__(self):
        return self.title
