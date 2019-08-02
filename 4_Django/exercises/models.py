from django.db import models

STYLE = (
    (-1, "not defined"),
    (0, "rock"),
    (1, "metal"),
    (2, "pop"),
    (3, "hip-hop"),
    (4, "electronic"),
    (5, "raegge"),
    (6, "other"),
)

STATUSY = (
    (1, "w trakcie pisania"),
    (2, "czeka na akceptację redaktora"),
    (3, "opublikowany"),
)

GWIAZDKI = (
    (1, " * "),
    (2, " ** "),
    (3, " *** "),
    (4, " **** "),
    (5, " ***** "),
)

# Create your models here.
class Band(models.Model):
    name = models.CharField(max_length=64)
    year = models.IntegerField(null=True)
    still_active = models.BooleanField(default=True)
    genre = models.IntegerField(choices=STYLE, default=-1)

    def __str__(self):
        return "{id} {name} {year}" .format(id=self.id, name=self.name, year=self.year, genre=self.genre)
    

class Category(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(null=False)

    def __str__(self):
        return " {id} ; {name} ; {description}" .format(id=self.id, name=self.name, description=self.description)

class Article(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=64, null=True)
    content = models.TextField
    date_added = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUSY)
    poczatek_emisji = models.DateTimeField(null=True)
    koniec_emisji = models.DateTimeField(null=True)
"""
    def __str__(self):
        return "{id} ;{title} ; {status}" .format(id=self.id, title=self.title, status=self.status)
"""

class Album(models.Model):
    band = models.ForeignKey(Band, on_delete=models.CASCADE)
    title = models.TextField
    rok_wydania = models.IntegerField
    ocena = models.IntegerField(choices=GWIAZDKI)

    def __str__(self):
        return "{id} {band}; {title}" .format(id=self.id, band=self.band, title=self.title)


class Song(models.Model):
    title = models.CharField(max_length=128)
    duration = models.TimeField(null=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return "{id} Tytuł: {title}, Album: {album}" .format(id=self.id, title=self.title, album=self.album)

class Person(models.Model):
    name =models.CharField(max_length=128)

    def __str__(self):
        return "{id} ; {name}" .format(id=self.id, name=self.name)

class Position(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE, primary_key=True)
    position_name = models.CharField(max_length=128)
    salary = models.DecimalField(max_digits=7, decimal_places=2)
    def __str__(self):
        return "{position_name} ; {salary}" .format(position_name=self.position_name, salary=self.salary)
    