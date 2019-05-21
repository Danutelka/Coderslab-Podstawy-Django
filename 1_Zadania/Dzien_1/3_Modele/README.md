<img alt="Logo" src="http://coderslab.pl/svg/logo-coderslab.svg" width="400">

# Modele &ndash; zadania

#### Pamiętaj, aby wszystkie modele definiować w pliku **models.py**!

#### Zadanie 1 &ndash; rozwiązywane z wykładowcą.

Zajrzyj do katalogu 4_Django. Znajdziesz tam projekt o nazwie **coderslab**. Sprawdź plik **settings.py**, czy wszystko jest skonfigurowane poprawnie. Utwórz wirtualne środowisko i zainstaluj potrzebne biblioteki. Wykonaj migrację i uruchom projekt.

#### Zadanie 2 &ndash; rozwiązywane z wykładowcą.

Zajrzyj do aplikacji **exercises** w projekcie **coderslab**. Znajdziesz tam model `Band`, który zawiera informację o zespołach rockowych. Znajdziesz tam zdefiniowane dwa pola: `name` &ndash; nazwę zespołu i `year` &ndash; rok założenia zespołu.

Dodaj tam pola:
* `still_active`: czy zespół jest jeszcze aktywny. Pole powinno przyjmować typ boolean, standardowa wartość `True`.
* `genre`: pole typu integer, które powinno przyjmować wartości:
    * -1: not defined,
    * 0: rock,
    * 1: metal,
    * 2: pop,
    * 3: hip-hop,
    * 4: electronic,
    * 5: reggae,
    * 6: other.

Pole powinno standardowo przyjąć wartość -1.

---

#### Zadanie 3.

Utwórz model `Category`, który będzie przechowywał listę wszystkich kategorii w CMS-ie. Model powinien mieć pola: 
* `name`: string, max 64 znaki,
* `description`: nielimitowanej długości string. Może przyjmować wartość `null`.

#### Zadanie 4.

a. Utwórz model `Article`, który będzie przechowywał dane nt. artykułów w CMS-ie. Model powinien mieć następujące pola:
* `title`: string, max. 128 znaków,
* `author`: string, max. 64 znaki, może przyjmować wartość `null`,
* `content`: nielimitowanej długości string,
* `date_added`: pole typu datetime, wartość ma być automatyczniee dodawana podczas pierwszego zapisu(tip: auto_now_add).

b. Model `Article` potrzebuje jeszcze kilku pól: 
* statusu, który będzie przyjmował następujące wartości:
    * w trakcie pisania,
    * czeka na akceptację redaktora,
    * opublikowany,
* daty początku emisji (pole może przyjmować wartość null),
* daty końca emisji (pole może przyjmować wartość null).

Zdefiniuj te właściwości, odpowiednio dobierając typy pól.

#### Zadanie 5.

Utwórz model `Album`, który będzie przechowywał następujące wartości:
* tytuł albumu,
* rok wydania,
* ocenę (w skali 0-5 gwiazdek).

Zdefiniuj te właściwości, odpowiednio dobierając typy pól.
