from django.db import models


class Album(models.Model):
	#defining Album atributes
	artist = models.CharField(max_length = 100)
	album_title = models.CharField(max_length = 200)
	genre = models.CharField(max_length=50)
	album_logo = models.CharField(max_length=1000)

	def __str__(self):
		return self.album_title + ' - ' + self.artist

class Song(models.Model):
	album = models.ForeignKey(Album, on_delete=models.CASCADE)
	file_type = models.CharField(max_length=20)
	song_title = models.CharField(max_length = 200)