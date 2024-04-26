# forum/forms.py

from django import forms
from .models import ForumTopic, ForumReply, ForumCategory

class ForumTopicForm(forms.ModelForm):
    class Meta:
        model = ForumTopic
        fields = ['category', 'title', 'content']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = ForumCategory.objects.all()

class ForumReplyForm(forms.ModelForm):
    class Meta:
        model = ForumReply
        fields = ['content']
