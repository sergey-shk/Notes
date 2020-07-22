from django.shortcuts import render
from .models import Note
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return render(request, 'note/not_auth.html')
    else:    
        user_notes = Note.objects.filter(author=request.user)
        context = {
            'notes': user_notes,
        }
        return render(request, 'note/home.html', context)


def new_note(request):
    return render(request, 'note/new_note.html')


def auth(request):
    return render(request, 'registration/login.html')
