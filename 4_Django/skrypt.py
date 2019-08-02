from exercises.models import Band
from exercises.models import Category
from exercises.models import Article

# zad 2
"""
b = Band.objects.filter(year=None)
print(b)

wyniki= Band.objects.filter(year=None)
for el in wyniki:
    el.year=1990
    el.save()
"""

#zad 3
"""
wynik = Band.objects.filter(genre=-1)
for i in wynik:
    i.gende = 6
    i.save()
"""

# zad 4
"""

b = Band.objects.filter(name__contains='The')
print(b)

Band.objects.filter(year__contains='98').filter(still_active=True)
Band.objects.filter(year__contains='97', name__contains='The')
Band.objects.filter(year__contains='98', still_active=False)
"""
# zad 5
"""
Category.objects.create(name="dobry", description="ujdzie")
Category.objects.create(name="zly", description="nie spelnia wymagan")

Article.objects.create(title="ahhso", author="wedwjd", content=". Him why feebly expect future now. ", status=1)
"""

"""
Album.objects.create(title="hahhha", rok_wydania=2018, ocena=5)

"""

# dzien2 zad 1
"""
Tworzenie obiektów Album:
a = Album()
a.title = ""
a.rok_wydania =""
a.ocena =""
a.band_id = "" - konieczne do podania po dodaniu relacji
a.save()
* zrobic migracje
"""

# dzien2 zad 3
"""
Album.objects.get(band_id=3) wszystkie albumy Bandu nr 3
Song.objects.get(album_id=9) wszystkie piosenki z albumu 9
"""

