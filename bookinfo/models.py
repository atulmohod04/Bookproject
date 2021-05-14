from django.db import models


# Create your models here.


class BookActiveManager(models.Manager):

    def get_queryset(self):
        return super(BookActiveManager, self).get_queryset().filter(is_delete=0)

class BookInactiveManager(models.Manager):

    def get_queryset(self):
        return super(BookInactiveManager, self).get_queryset().filter(is_delete=1)
    

class Book(models.Model):

    name = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    prize= models.CharField(max_length=150)
    publication = models.CharField(max_length=150)
    is_delete = models.IntegerField(default=0)
    book_objects = models.Manager()
    active_objects = BookActiveManager()
    Inactive_objects = BookInactiveManager()





    class Meta:
        db_table= 'book'

    def __str__(self):
        return self.name

    # git code
    def git():
        print("1")
           # git code
    def git():
        print("3")