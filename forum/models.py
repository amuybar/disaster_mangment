# forum/models.py

from django.db import models
from django.contrib.auth.models import User

class ForumCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ForumTopic(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(ForumCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class ForumReply(models.Model):
    content = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    topic = models.ForeignKey(ForumTopic, on_delete=models.CASCADE, related_name='replies')

    def __str__(self):
        return f"Reply by {self.created_by} on {self.topic.title}"
