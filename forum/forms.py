# forum/forms.py

from django import forms
from .models import ForumTopic, ForumReply

class ForumTopicForm(forms.ModelForm):
    class Meta:
        model = ForumTopic
        fields = ['title', 'content']

class ForumReplyForm(forms.ModelForm):
    class Meta:
        model = ForumReply
        fields = ['content']
