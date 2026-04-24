from django.shortcuts import render
from .models import GlobalMessage

def global_chat(request):
    messages = GlobalMessage.objects.select_related('user').order_by('created_at')
    return render(request, 'global-chat/global_chat.html', {
        'messages': messages
    })
