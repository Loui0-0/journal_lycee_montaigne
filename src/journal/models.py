from django.db import models

# Create your models here.

class Articles(models.Model):
	article_path = models.CharField(max_length=200)
	title = models.CharField(max_length=200)
	author = models.CharField(max_length=50)
	date = models.DateField()
 