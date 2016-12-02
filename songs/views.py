from django.shortcuts import render, redirect
from django.http import HttpResponse

from songs.forms import SongForm
from songs.models import Song


def index(request):
    song_list = Song.objects.order_by('-created')
    form = SongForm()
    context = {
        'song_list': song_list,
        'form': form,
    }
    return render(request, 'songs/index.html', context)


def index2(request):
    song_list = Song.objects.order_by('-created')
    form = SongForm()
    context = {
        'song_list': song_list,
        'form': form,
    }
    return render(request, 'songs/index2.html', context)


def detail(request, song_id):
    return HttpResponse("You're looking at question %s." % question_id)


def add(request):
    if request.method == 'POST':
        title = request.POST['title'] if request.POST['title'] else None
        author = request.POST['author'] if request.POST['author'] else None
        link = request.POST['link'] if request.POST['link'] else None

        Song(title=title, author=author, link=link).save()

    return redirect('/songs/')


def vote(request, song_id):
    return HttpResponse("You're voting on question %s." % question_id)