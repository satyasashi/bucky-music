from django.db import models

# Create your models here.
class Album(models.Model):
	artist = models.CharField(max_length=250)
	albumTitle = models.CharField(max_length=200)
	genre = models.CharField(max_length=100)
	albumLogo = models.CharField(max_length=500)

	def __str__(self):
		return self.albumTitle + "-" + self.artist

class Song(models.Model):
	album = models.ForeignKey(Album, on_delete=models.CASCADE)
	file_type = models.CharField(max_length=10)
	song_title = models.CharField(max_length=200)
	is_favorite = models.BooleanField(default=False)

	def __str__(self):
		return self.song_title