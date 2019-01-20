from django.db import models

# Create your models here.

class Book(models.Model):
    isbn = models.CharField(max_length=16)
    name = models.CharField(max_length=512)
    author = models.CharField(max_length=256)
    course = models.CharField(max_length=128)
    publisher = models.CharField(max_length=512)
    hardcover = models.NullBooleanField()
    want = models.BooleanField()
    version = models.CharField(max_length=128)
    id = models.CharField(max_length=36, primary_key=True)
    sold = models.BooleanField()
    poster = models.EmailField()

class Comment(models.Model):
    id = models.CharField(max_length=36, primary_key=True)
    target = models.ForeignKey(Book, on_delete=models.CASCADE)
    poster = models.EmailField()
    buyer = models.EmailField()
    time = models.DateTimeField()
    text = models.TextField()
