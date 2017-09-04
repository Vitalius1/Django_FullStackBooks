from __future__ import unicode_literals

from django.db import models

class BookManager(models.Manager):
    def make_book(self, title, author, category):
        self.create(title = title, category = category, author = author)
        return
    def show_book(self):
        all_books = self.all()
        return all_books

class Book(models.Model):
    title = models.CharField(max_length = 45)
    author = models.CharField(max_length = 45)
    category = models.CharField(max_length = 45)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = BookManager()
    def __str__(self):
        return self.title + " " + self.author + " " + self.category


# Create your models here.
