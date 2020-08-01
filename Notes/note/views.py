from django.shortcuts import render
from .models import Note
from django.contrib.auth.models import User
from .forms import NoteForm
from django.shortcuts import redirect
import datetime
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
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
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.author = request.user
            note.pub_date = timezone.now()
            note.date = timezone.now()
            note.save()
            return redirect('index')
    else:
        form =  NoteForm()
    return render(request, 'note/new_note.html', {'form': form})

def edit_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save(commit=False)
            note.author = request.user
            note.published_date = timezone.now()
            note.save()
            return redirect('index')
    else:
        form = NoteForm(instance=note)
    return render(request, 'note/new_note.html', {'form': form})


def del_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    note.delete()
    return redirect('index')

def auth(request):
    return render(request, 'registration/login.html')


def signup(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      form.save()
    return redirect('index')
  else:
    form = UserCreationForm()
    return render(request, 'note/signup.html', {'form': form})
