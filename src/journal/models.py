from django.db import models

# Create your models here.

class Articles(models.Model):
	article = models.FileField(upload_to='articles/')
	title = models.CharField(max_length=200)
	author = models.CharField(max_length=50)
	date = models.DateField()
	def __str__(self):
		return f'{self.title} de {self.author} le {self.date} {self.article}'