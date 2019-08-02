from django.db import models


GWIAZDKI = (
    (1, " * "),
    (2, " ** "),
    (3, " *** "),
    (4, " **** "),
    (5, " ***** "),
)


# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=32, default="No")
    last_name = models.CharField(max_length=32, default="Name")

    def __str__(self):
        return "{first_name}; {last_name} " .format(first_name=self.first_name, last_name=self.last_name)
    
class Genre(models.Model):
    name = models.CharField(max_length=32, default="None")

    def __str__(self):
        return "{name}" .format(name=self.name_string)
    
class Movie(models.Model):
    title = models.CharField(max_length=128)
    director = models.ForeignKey('Person', related_name='movie_director', on_delete=models.CASCADE)
    screenplay = models.ForeignKey('Person',related_name='movie_screenplay', on_delete=models.CASCADE)
    starring = models.ManyToManyField('Person')
    year = models.IntegerField(null=True)
    rating = models.DecimalField(max_digits=4, decimal_places=2, null=True,blank=True)
    genre = models.ManyToManyField('Genre')

    def __str__(self):
        return "{title} {director} {screenplay} {year} {rating} {genre}".format(
            title=self.title,
            director=self.director,
            screenplay=self.screenplay,
            # starring=self.starring.all(),
            year=self.year,
            rating=self.rating,
            genre=self.genre.all(),
        )
        
class PersonMovie(models.Model):
    role = models.CharField(max_length=128, null=True)
    person = models.OneToOneField('Person', on_delete=models.CASCADE)

    # movie = models.OneToOneField('Movie', on_delete=models.CASCADE)

    def __str__(self):
        return "{role} {aktor} {movie}".format(role=self.role,
                                               aktor=self.person)