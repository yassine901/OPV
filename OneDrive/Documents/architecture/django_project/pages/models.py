from django.db import models

# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=64,unique=True)
class Book(models.Model):
    title=models.CharField(max_length=32, unique=True)
    quantity=models.IntegerField(default=1)
    author=models.ForeignKey(Author, on_delete=models.DO_NOTHING)  

class Book(models.Model):
    title = models.CharField(max_length=32, unique=True)
    quantity = models.IntegerField(default=1)
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
    class Meta:
        verbose_name="Livre"
        verbose_name_plural= "Livres"
    def __str__(self):
        return self.title