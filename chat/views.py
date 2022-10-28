from django.shortcuts import render
from message.models import Message

# Create your views here.

def lobby(request):
    return render(request, 'chat/lobby.html', {'messages': Message.objects.all()})