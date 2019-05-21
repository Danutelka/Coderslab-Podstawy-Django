<img alt="Logo" src="http://coderslab.pl/svg/logo-coderslab.svg" width="400">

# Zaawansowane URL-e

### Zadanie 1.
Zmień routing dla zadań 1-3 z działu "Widoki" w następujący sposób:
* W zadaniu 1 zmienna `max number` musi być liczbą i posiadać od 2 do 4 cyfr,
* W zadaniu 2 zmienna `max number` musi być liczbą i posiadać dokładnie 4 cyfry, a zmienna `min number` musi mieć dokładnie 2 cyfry,
* W zadaniu 3 zmienna `name` musi składać się z tylko liter i zaczynać z dużej litery. 
 
### Zadanie 2.

Popraw istniejące widoki, w których parametry przekazywane są przez GET w taki sposób, żeby były podawane w URL-ach.

### Zadanie 3 (*).

* Napisz widok `show_team_statistics`, który pokaże:
    * nazwę klubu,
    * sumę goli zdobytych,
    * sumę goli straconych,
    * liczbę meczów u siebie,
    * liczbę meczów na wyjeździe.
* zdefiniuj URL (w pliku **urls.py**), który będzie miał następujący schemat:
```/stats/<team-id>```, gdzie **team_id**, to identyfikator klubu,

#### Pamiętaj, że odbieranie danych zapisanych w tak zdefiniowanym URL-u odbywa się inaczej niż do tej pory!

