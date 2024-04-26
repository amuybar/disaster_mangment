from django.db import models
from django.conf import settings


class ForumCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ForumTopic(models.Model):
    category = models.ForeignKey(ForumCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class ForumReply(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    topic = models.ForeignKey(ForumTopic, on_delete=models.CASCADE, related_name='replies')
    def __str__(self):
        return self.content
