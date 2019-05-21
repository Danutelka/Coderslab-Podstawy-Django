<img alt="Logo" src="http://coderslab.pl/svg/logo-coderslab.svg" width="400">

# Przekazywanie informacji między stronami: sesje.
Upewnij się, czy frameworki sesji są podłączone do aplikacji (plik **settings.py**),

### Zadanie 1.
W zadaniu stwórz trzy widoki, które mają mieć następującą funkcjonalność:
* Pierwszy widok ma być przypisany pod adres `/setSession` ma nastawiać informacje w sesji pod kluczem ```counter``` na **0**.
* Drugi widok ma być przypisany pod adres `/showSession`  wyświetlać zawartość sesji pod kluczem ```counter``` i zwiększać ją o **1**. Jeżeli nie ma takich danych w sesji, to strona powinna wyświetlić odpowiednie informacje.
* Trzeci widok ma być przypisany pod adres `/deleteSession`  kasować dane z sesji (tylko te trzymane pod kluczem ```counter```).

### Zadanie 2.
Napisz widok przypisany pod adres `/login`. Widok ten powinien:
* W przypadku w którym wejdziemy na niego metodą GET wyświetlić formularz do logowania:  
```html
<form action="" method="POST">
    <label>
        Imię:
        <input type="text" name="name">
    </label>
    <input type="submit">
    {% csrf_token %}
</form>
``` 
* W przypadku przesłania danych POST do sesji pod kluczem `loggedUser` wpisz przesłane imię.
* W przypadku w którym wejdziemy na niego metodą GET, a sesji są informacji pod kluczem `loggedUser` wyświetl komunikat `Witaj <imię>` - ta część polecenia wymaga modyfikacji kodu napisanego w pierwszym punkcie.

### Zadanie 3.
Napisz widok pod adresem `/addToSession` który wyświetli następujący formularz:  
```html
<form action="#" method="POST">
    <label>
        Klucz:
        <input type="text" name="key">
    </label>
    <label>
        Wartość:
        <input type="text" name="value">
    </label>
    <input type="submit">
    {% csrf_token %}
</form>
  ``` 
W przypadku wejścia na tą stronę metodą POST widok powinien dodawać do sesji przesłaną wartość (pod odpowiedni klucz).  
Następnie napisz widok pod adresem `/showAllSession` który wyświetli w formie tabeli wszystkie dane znajdujące się w sesji (zarówno klucz jak i wartość). 

### Zadanie 4 (*).

* zmodyfikuj widok `add_game` tak, aby zapamiętać w sesji, który zespół był ostatnio edytowany (jako gospodarz),
* podczas ponownego wejścia na stronę odczytać zmienną sesyjną i ustawić listę HTML na pozycji odpowiadającej ostatnio edytowanemu klubowi (`<option ... selected>`)
