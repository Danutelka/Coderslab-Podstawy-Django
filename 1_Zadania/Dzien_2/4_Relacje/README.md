<img alt="Logo" src="http://coderslab.pl/svg/logo-coderslab.svg" width="400">

# Relacje &ndash; zadania

##### Wszystkie zadania wykonuj używając Django ORM.

#### Zadanie 1 &ndash; wykonywane razem z wykładowcą.
* W części 1, utworzyliście model `Album`. Teraz dodaj odpowiednią relację z modelem `Band`, tak by jeden zespół mógł mieć wiele albumów.

* Dodaj kilka albumów do kilku zespołów (nie szukaj ich w internecie, możesz coś wymyślić). 

* Wypisz w konsoli wszystkie albumy dowolnego zespołu.

---

#### Zadanie 2.

Dodaj do modeli kolejny: `Song`. Powinien mieć następujące pola:
* `title`: string, max długość 128 znaków,
* `duration`: czas (TimeField), może przyjmować null,
* dodaj relację wiele-do-jednego tak, aby jeden album mógł mieć wiele piosenek.

Uzupełnij dane, tworząc albumy grup i uzupełniając je piosenkami (nie przejmuj się, czy piosenki są prawdziwe, po prostu je dodaj).

#### Zadanie 3.

Wyciągnij z bazy danych (i wypisz na konsoli), używając modeli:

* wszystkie albumy dowolnego zespołu,
* wszystkie piosenki z każdego albumu.

#### Zadanie 4.

* Połącz modele `Article` i `Category` tak, aby jeden artykuł mógł mieć wiele kategorii, a każda kategoria mogła być przypisana do wielu tytułów.
* Dodaj kilka kategorii do każdego artykułu.

#### Zadanie 5.

* Wybierz kategorię. Następnie wybierz (i wypisz na konsoli) wszystkie artykuły należące do tej kategorii.
* Wybierz dwie kategorie. Następnie wybierz i wypisz na konsoli wszystkie artykuły należące *jednocześnie* do obu kategorii.

#### Zadanie 6.
* Napisz model `Person`, który będzie miał następującą właściwość:
    * `name`,
* Napisz model `Position`, który będzie miał następujące właściwości:
    * `position_name`,
    * `salary`,
* Połącz oba modele relacją tak, aby jedna osoba mogła być przypisana dokładnie do jednego stanowiska, a każde stanowisko miało tylko jednego pracownika. Zadbaj o to, by wraz z usunięciem stanowiska, usuwana była też przyporządkowana do niego osoba.
Hint:
Masz dwa sposoby:
- albo dodajesz pole `person` w modelu `Position`
- albo dodajesz pole `position` w modelu `Person`

* Dodaj kilka osób i stanowisk.


#### Zadanie 7.

Napisz widok i udostępnij go pod adresem `/show_band/{id}`, gdzie **id** to identyfikator zespołu. Widok powinien wyświetlić informacje o zespole muzycznym: jego nazwę, gatunek i rok założenia oraz informację, czy wciąż jest aktywny. 

W tym celu w widoku musisz pobrać parametrem z URL-a id zespołu, wyciągnąć przy użyciu modelu dane zespołu i przekazać je kontekstowo do szablonu. 

Zwróć uwagę, że jeśli w zadaniu 1 dodałeś klucz obcy Band - Album, to w modelu `Band` masz pole, które przechowuje listę albumów danego zespołu. Pokaż albumy w szablonie. 

**Hint:** użyj następującego wyrażenia regularnego, do zdefiniowania URL-a: 
```
^/show_band/(?P<id>\d+)
```



### Zadanie 8 (*).
1. utwórz aplikację **football** i zarejestruj ją w projekcie,
2. do bazy danych zaimportuj strukturę i dane z pliku **football.sql** dołączonego do ćwiczeń. Zapoznaj się z bazą danych, jej tabelami i danymi.
3. utwórz widok `league_table`, który:
    * wyciągnie z bazy danych ligową tabelę posortowaną wg liczby zdobytych punktów,
    * utworzy HTML, w którym znajdą się następujące dane:
        * pozycja w tabeli,
        * nazwa klubu,
        * liczba punktów,
    * zwróci wynik do przeglądarki.
4. utwórz wpis w pliku **urls.py**, który udostępni aplikacji widok `league_table` pod URL-em `/table`.

### Zadanie 9 (*).
1. wybierz swój ulubiony klub piłkarski z tabeli (np. Naprzód Brwinów),
2. utwórz widok `games_played`, który:
    * wyciągnie z tabeli wszystkie mecze, które rozegrał klub (zarówno te w domu, jak i na wyjeździe),
    * utworzy HTML, w którym znajdą się następujące dane:
        * nazwa klubu gospodarza,
        * nazwa klubu gościa,
        * wynik (np. 2:0).
    * zwróci wynik do przeglądarki.
3. utwórz wpis w pliku **urls.py**, który udostępni aplikacji widok `games_played` pod URL-em `/games`.

**Podpowiedzi do zadań 8 i 9:** 

* Do operacji na bazach danych użyj modeli.

* Zapoznaj się z materiałami pod poniższymi linkami. Dowiesz się, jak poradzić sobie z tworzeniem modeli do istniejących już baz danych:
    * https://docs.djangoproject.com/en/1.11/ref/django-admin/#inspectdb  
    * https://docs.djangoproject.com/en/1.11/howto/legacy-databases/

* Z jakiegoś powodu dla pewnych konfiguracji inspectdb może nie działać prawidłowo. Gdyby tak się działo, niestety trzeba skorzystać z gotowego rozwiązania:

```python
class Games(models.Model):
    id = models.BigAutoField(primary_key=True)
    team_home = models.ForeignKey('Teams', models.DO_NOTHING, db_column='team_home', blank=True, null=True)
    team_home_goals = models.BigIntegerField(blank=True, null=True)
    team_away = models.ForeignKey('Teams', models.DO_NOTHING, db_column='team_away', blank=True, null=True)
    team_away_goals = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'games'


class Teams(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    points = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'teams'
```

