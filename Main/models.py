from django.db import models

# Create your models here.

class Book():
	isbn = models.CharField(max_length=16)
	name = models.CharField(max_length=512)
	author = models.CharField(max_length=256)
	class = models.CharField(max_length=128)
	publisher = models.CharField(max_length=512)
	hardcover = models.NullBooleanField()
	version = models.CharField(max_length=128)
	id = models.CharField(max_length=16, primary_key=True)
	sold = models.BooleanField()

class Comment():
	id = models.CharField(max_length=16, primary_key=True)
	target = models.ForeignKey(Book, on_delete=models.CASCADE)
	buyer = models.EmailField()
	time = models.DateTimeField()
	text = models.TextField()
