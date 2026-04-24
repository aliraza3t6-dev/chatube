from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Message


@login_required
def chatroom(request, username):
    r = User.objects.filter(username=username).first()

    messages = Message.objects.filter(
        (Q(sender=request.user) & Q(receiver=r)) |
        (Q(sender=r) & Q(receiver=request.user))
    ).order_by("timestamp")

    return render(
        request,
        "chat/chat.html",
        {
            "r": r,
            "messages": messages
        }
    )
