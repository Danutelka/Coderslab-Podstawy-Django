<img alt="Logo" src="http://coderslab.pl/svg/logo-coderslab.svg" width="400">

# Widoki jako funkcje / proste URL-e.

### Zadanie 1.
Napisz widok który będzie przypisany do adresu `/random/<max number>` gdzie `max number` powinno być liczbą (na razie nie przejmuj się walidacją - po prostu przyjmij zmienną). Strona ta powinna pokazywać losową liczbę z zakresu od 0 do liczby podanej przez użytkownika. Strona powinna wyświetlać napis `Użytkownik podał wartość <max number>. Wylosowano liczbę: <wylosowana liczba>` oczywiście wstawiając odpowiednie zmienne w odpowiednie miejsca. 

Hint: Wyrażenie regularne do pliku **urls.py**
```
r'^random/(?P<max_number>(\d)+)$'
```

### Zadanie 2.
Napisz widok który będzie przypisany do adresu `/random/<min number>/<max number>` gdzie `min number` i `max number` powinny być liczbami (na razie nie przejmuj się walidacją - po prostu przyjmij zmienną). Strona ta powinna pokazywać losową liczbę z zakresu podanego przez użytkownika. Strona powinna wyświetlać napis `Użytkownik podał wartośći <min number> i <max number>. Wylosowano liczbę: <wylosowana liczba>` oczywiście wstawiając odpowiednie zmienne w odpowiednie miejsca.  
Zauważ jak w zależności od różnej ilości parametrów wykonywane są widoki z zadań 1, 2 lub 3 (z poprzedniego działu). 

Hint: Wyrażenie regularne do pliku **urls.py**
```
r'^random/(?P<min_number>(\d)+)/(?P<max_number>(\d)+)$'
```
    
### Zadanie 3.
Napisz widok który będzie przypisany do adresu `/hello/<name>` gdzie `name` powinno być ciągiem znaków (na razie nie przejmuj się walidacją - po prostu przyjmij zmienną). Strona ta powinna pokazywać napis `Witaj <name>` oczywiście wstawiając odpowiednią zmienną w odpowiednie miejsce.

Hint: Wyrażenie regularne do pliku **urls.py**
```
r'^hello/(?P<name>([A-Za-z])+)$
```
