<img alt="Logo" src="http://coderslab.pl/svg/logo-coderslab.svg" width="400">

# Podstawy Django -- praca domowa

W repozytorium przygotowany jest katalog `4_Django`. W tym projekcie jest aplikacja `homework` - w tej aplikacji wykonuj swoje prace domowe.

## Dzień 1.

### Zadanie 1. 

Wyobraź sobie serwis filmowy w stylu FilmWeb albo IMDB. Będziemy zbierać informacje o filmach i ludziach pracujących w filmie. W tym celu zdefiniuj następujace obiekty:

* `Person` a w nim następujące pola:
    * `first_name` string o max długości 32 znaki,
    * `last_name` string o max długości 32 znaki.
    
* `Genre` a w nim następujące pola:
    * `name` string o max długości 32 znaki,
    
* `Movie` czyli opis filmu, a w nim następujące pola:
    * `title`: string o max długości 128 znaków,
    * `director`: klucz obcy do modelu `Person`,
    * `screenplay`: klucz obcy do modelu `Person`.
    * `starring`: relacja wiele-do-wielu z modelem `Person`. Relacja powinna mieć dodatkowe pole `role` (string 128 znaków, może być null), czyli rola jaką gra aktor w filmie, tabela przechodnia powinna mieć nazwę `PersonMovie`, 
    * `year`: integer, rok produkcji filmu,
    * `rating`: float, ocena filmu: liczba od 1.0 do 10.0.
    * `genre` relacja wiele-do-wielu z modelem `Genre`.
Wypełnij modele danymi: zdefiniuj kilka osób: reżyserów, scenarzystów, aktorów. Dodaj kilka filmów.

### Zadanie 2.

* Napisz widok, który udostępnisz pod adresem `/movies`. Wypisze on listę tytułów filmowych posortowanych od najnowszego do najstarszego oraz rok produkcji, nazwisko reżysera i ocena. Tytuł filmu powinien być linkiem do URL-a `/movie_details/{id}` gdzie id to identyfikator filmu.

### Zadanie 3.

Napisz widok, który udostępnisz pod adresem `/movie_details/{id}` gdzie id to identyfikator filmu. Widok pobierze dane o filmie z bazy (używając modelu) i wyświetli na stronie wszystkie posiadane informacje o filmie.

## Dzień 2.

### Zadanie 4.

* Dodaj widoki: 
    * `/persons` - lista osób: przy nazwisku każdej osoby powinien być link do edycji. Parametr powinien być przekazywany w URL-u. Na dole listy osób powinien być link "dodaj osobę".
    * `/edit_person/{id}` - edycja osoby: po wejściu na link do edycji wyświetla się formularz edycji osoby. Można zmienić dane i zapisać.
    * `/add_person` - dodawanie osoby: po wejściu w link "dodaj osobę", powinien wyświetlić się pusty formularz, w którym można dodać nową osobę i zapisać. Po prawidłowym dodaniu osoby powinniśmy zostać przniesieni pod adres `/persons`.
    
### Zadanie 5.

* Zmodyfikuj widok `/movies`
    * obok tytułu filmu dodaj link do edytowania filmu, parametr powinien być przekazany w URL-u. Po kliknięciu w ten link program powinen wyciągnąć dane o tym filmie z bazy, a następnie pokazać formularz edycji filmu wypełniony danymi wybranego filmu. Film można zapisać do bazy. Strona edycji powinna być udostępniona pod adresem `/edit_movie/{id}`
    * na dole listy filmów dodaj link "Dodaj film". Po kliknięciu w ten link powinien pokazać się pusty formularz dodawania filmu. Film można zapisać do bazy. Strona edycji powinna być udostępniona pod adresem `/add_movie`. Po prawidłowym dodaniu filmu do bazy powinno nastąpić przekierowanie pod adres `/movies`,

## Dzień 3.

### Zadanie 6.
Przerób widok `/movies` tak, aby:
* na górze strony znajdowały się trzy przyciski do sortowania listy filmów wg. ich oceny (rosnąco, malejąco lub domyślnie), po naciśnięciu przycisku strona powinna się odświeżyć, pokazać posortowaną listę filmów oraz zapisać do sesji pod kluczem `sorted` wartość: 
   * `1` jeżeli wybrana została opcja malejąca (od najwyższej do najniższej oceny), 
   * `2` jeżeli wybrana została opcja rosnąca (od najniższej do najwyższej oceny),
   * `0` jeżeli została wybrana opcja domyślna (sortowanie domyślne wg roku produkcji, tak jak w zadaniu 2.),

* po ponownym wejściu na stronę lista była posortowana zgodnie z ostatnim wyborem

### Zadanie 7.
Napisz widok `/search_movie`, pod którym:

* widoczny będzie formularz, dzięki któremu można będzie wyszukiwać filmy, w formularzu powinny znajdować się następujące pola (użyj odpowiednich wartości dla atrybutu `name`):
   * `title` nazwa filmu - `name="title"`, 
   * `first_name` imię osoby - `name="first_name"`,
   * `last_name` nazwisko osoby - `name="last_name"`,
   * `year`rok - od `name="year_from"` do - `name="year_to"`,
   * `genre` gatunek - `name="genre"`, 
   * `rating` ocena - od `name="rating_from"` do - `name="rating_to"`.

* dodatkowe wymagania:
   * powinno być możliwe wyszukiwanie od-do wg roku produkcji, 
   * powinno być możliwe wyszukiwanie od-do wg oceny filmu,
   * powinno być możliwe wpisanie po przecinku kilku gatunków w polu `genre` i wyszukanie wszystkich filmów, które są przypisane do tych gatunków,
   * po wpisaniu imienia lub nazwiska w polu `person` mają być wyszukane wszystkie filmy, w których szukana osoba pełni jakąś rolę (jest reżyserem, scenarzystą, aktorem),
   * puste pole w wysłanym formularzu powinno oznaczać "wszystkie dane", tzn. wysłanie całkowicie pustego formularza powinno wyszukać wszystkie dostępne w bazie filmy; wpisanie w polu `last_name` wartości `Smith`i zostawienie pozostałych þól pustych powinno wyszukać wszystkie filmy, w których jakąkolwiek rolę pełnią osoby o nazwisku `Smith`.

Wyniki wyszukiwania powinny pojawiać się na tej samej stronie tzn. `/search_movie`.

## Dzień 4.

### Zadanie 8.
Nadaj wszystkim URL-om etykietki (trzeci argument w definicji URL-a). Pamiętaj, że etykiety powinny być unikalne. (Jeśli masz wątpliwości jak to zrobić, zajrzyj tutaj: https://docs.djangoproject.com/en/1.10/topics/http/urls/#reverse-resolution-of-urls)


### Zadanie 9.
Przerób widoki tak, aby w linkach odwoływały się do etykietek. (Jeśli masz wątpliwości jak to zrobić, zajrzyj tutaj: https://docs.djangoproject.com/en/1.10/topics/http/urls/#reverse-resolution-of-urls)


### Zadanie 10.
Przerób widoki `/persons` oraz `/movies` tak, aby spełniały następujące warunki:
* przy nazwisku każdej osoby oraz przy tytule każdego filmu powinny znajdować się przyciski pozwalające na usunięcie osoby i filmu
* przyciski powinny przekierowywać pod adresy: `/del_person/{id}` dla osoby oraz `/del_movie/{id}` dla filmu.
* po poprawny usunięciu osoby oraz filmu, na ekranie powinien pojawić się komunikat `Usunięto osobę!` lub `Usunięto film!`

### Zadanie 11.
Upewnij się, że serwis filmowy jest spójny graficznie. Na każdej stronie powinno znajdować się menu pozwalające na łatwe nawigowanie po całym serwisie (odnośniki do listy osób, listy filmów, formularza wyszukiwania)
