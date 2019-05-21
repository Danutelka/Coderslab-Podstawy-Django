<img alt="Logo" src="http://coderslab.pl/svg/logo-coderslab.svg" width="400">

# Dodawanie i wyszukiwanie danych &ndash; zadania

##### Wszystkie zadania wykonuj używając Django ORM.

#### Zadanie 1 &ndash; wykonywane razem z wykładowcą.

W aplikacji **exercises**, w modelu `Band` znajduje się kilkanaście zespołów. 

* Wyciągnij dane wszystkich zespołów.
* Posortuj je alfabetycznie.
* Dodaj dane zespołu Rage Against The Machine, rok założenia 1991.

---

#### Zadanie 2.

* Znajdź wszystkie zespoły, które nie mają zdefinowanego roku założenia. Wypisz w konsoli ich nazwy i identyfikator nadany przez bazę danych.
* Znajdź informacje o zespołach, które nie mają w naszej bazie podanego roku założenia. Uzupełnij informacje (może być losowo) i zapisz je w bazie danych.

##### Napisz program w Pythonie, który wykona te zadania.

#### Zadanie 3.

* Uzupełnij gatunki zespołów oraz informację, czy są nadal aktywne. 

##### Napisz program w Pythonie, który wykona te zadania.

#### Zadanie 4.

Znajdź i wypisz na konsoli wszystkie zespoły, które:

* Mają w nazwie "The",
* założone zostały w latach 1980-tych i są wciąż aktywne,
* założone zostały w latach 1970-tych oraz mają w nazwie "The",
* założone zostały w latach 1980-tych, oraz są już nieaktywne. 

#### Zadanie 5.

* Do modelu `Category` z poprzedniej części, dodaj kilka wybranych kategorii,
* Dodaj kilka artykułów do modelu `Article`.

Nie dodawaj tytułu ani zawartości losowo, skorzystaj z http://randomtextgenerator.com/

#### Zadanie 6.

Napisz widok, który udostępnisz pod adresem `/articles`, w którym pokażesz listę artykułów. Na liście powinien pojawić się tytuł, autor (jeśli jest) i data dodania artykułu do bazy. Wybierz tylko artykuły ze statusem "opublikowany".

W tym celu w widoku wyciągnij wszystkie opublikowane artykuły z bazy danych, i przekaż je kontekstem do szablonu, który wyświetli odpowiednio dane.
