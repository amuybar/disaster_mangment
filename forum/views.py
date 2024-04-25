from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ForumCategory, ForumTopic, ForumReply
from .forms import ForumTopicForm, ForumReplyForm

@login_required
def forum(request):
    categories = ForumCategory.objects.all()
    return render(request, 'forum.html', {'categories': categories})

@login_required
def create_topic(request):
    if request.method == 'POST':
        form = ForumTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.created_by = request.user
            topic.save()
            return redirect('forum')
    else:
        form = ForumTopicForm()
    return render(request, 'create_topic.html', {'form': form})

@login_required
def view_topic(request, topic_id):
    topic = get_object_or_404(ForumTopic, pk=topic_id)
    replies = ForumReply.objects.filter(topic=topic)
    if request.method == 'POST':
        form = ForumReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.created_by = request.user
            reply.topic = topic
            reply.save()
            return redirect('view_topic', topic_id=topic_id)
    else:
        form = ForumReplyForm()
    return render(request, 'view_topic.html', {'topic': topic, 'replies': replies, 'form': form})
