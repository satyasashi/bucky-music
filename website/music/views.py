from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Album

# Create your views here.
def index(request):
	all_albums = Album.objects.all()
	context = {'all_albums': all_albums,}
	return render(request, 'music/index.html', context)

# detail function, passing album_id regex group as param
def detail(request, album_id):
	album = get_object_or_404(Album, pk=album_id)
	return render(request, 'music/detail.html', {'album':album,})

# Favorite song view
def favorite(request, album_id):
	album = get_object_or_404(Album, pk=album_id)
	try:
		selected_song = album.song_set.get(pk=request.POST['song']) # gets id of song
		print(request.POST['song'])
	except (KeyError, Song.DoesNotExist):
		return render(request, 'music/detail.html', {
			'album': album, 
			'error_message': "You did not enter valid song",
			})
	else:
		selected_song.is_favorite = True
		selected_song.save()
		return render(request, 'music/detail.html', {'album': album,})