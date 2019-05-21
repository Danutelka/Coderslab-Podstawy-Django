<img alt="Logo" src="http://coderslab.pl/svg/logo-coderslab.svg" width="400">

# Przekazywanie informacji pomiędzy stronami: formularze i POST.

### Zadanie 1.    
Napisz widok który w przypadku wejścia metodą GET wyświetli formularz przyjmujący imię i nazwisko. Formularz ten ma przekierowywać na ten sam adres metodą POST.
Jeżeli strona została uruchomiona przez zapytanie POST, to ponad formularzem ma się wyświetlić napis `Witaj, <podane imię> <podane nazwisko>`.  

Hint: żeby sprawdzić jaką metodą została uruchomiona strona możesz wykorzystać poniższy kod:
```python
if request.method == "GET":
    do_something()
elif request.method == "POST":
    do_something_else()
```
Hint 2: żeby formularz przekierowywał do tej samej strony możesz zostawić jego pole action puste.

### Zadanie 2.
Napisz widok który będzie przeliczał temperaturę z stopniach Celsjusza na temperaturę w stopniach Fahrenheita (i w drugą stronę). Skorzystaj z poniższego formularza:  
```html
<form action="" method="POST">
    <label>
        Temperatura:
        <input type="number" min="0.00" step="0.01" name="degrees">
    </label>
    <input type="submit" name="convertionType" value="celcToFahr">
    <input type="submit" name="convertionType" value="FahrToCelc">
</form>
``` 

Formularz ma dwa guziki submit, z tą samą nazwą (atrybut `name` nastawiony na wartość `convertionType`) ale inną wartością (atrybut `value`). Żeby przekonać się który guzik został wciśnięty zobacz jaka będzie wartość w obiekcie `HttpRequest.POST` pod kluczem `convertionType`. Żeby przeliczyć jednostki użyj wzorów znajdujących się [tutaj][degrees-convertion].

**Podpowiedź:** Widok będzie oczekiwał tokena CSRF i jeśli go nie znajdzie, zgłosi błąd i nie przepuści użytkownika dalej. Aby temu zapobiec (tylko na potrzeby ćwiczenia, CSRF to dość skuteczne zabezpieczenie przed włamaniami na stronę), należy użyć dekoratora:

```python
@csrf_exempt
def my_view(request):
    . . . 
```

### Zadanie 3 (*).
1. Napisz formularz, w którym przyjmiesz następujące informacje:
    * klub piłkarski, grający mecz u siebie (niech będzie to rozwijalna lista, gdzie wartością pola będzie ID klubu, a opisem nazwa - odpowiednie dane wczytaj z bazy danych),
    * klub piłkarski, grający mecz na wyjeździe (j.w.),
    * wynik (najłatwiej będzie to zrobić w formie dwóch pól),
2. Formularz ma ustawić przesyłanie danych metodą POST na adres `/add_game`.
3. Napisz widok `add_game` (udostępnij go pod URL-em `/add_game`), który:
    * odbierze dane z formularza napisanego w poprzednim punkcie,
    * sprawdzi, czy dane wyniku są prawidłowe (czy są poprawnymi liczbami całkowitymi),
    * zapisze dane do bazy danych (do tabelki `Games`),
    * w przypadku prawidłowych danych przekieruje użytkownika do stronę z meczami klubu gospodarza,
    * w przypadku błędnych danych pokaże informacje o błędzie (w przeglądarce).

### Zadanie 4 (*).
Zmodyfikuj widok `/add_game` tak, aby na podstawie wyniku modyfikował liczbę punktów, które zdobył klub:
* za zwycięstwo: 3pkt,
* za remis: 1 pkt.

Liczba punktów jest trzymana w tabeli `Teams`.

### Zadanie 5 (*).
Napisz widok `modify_team` (udostępnij go pod URL-em `/modify_team?id=<id>`), który:
* pobierze z URL-a ID klubu,
* utworzy formularz z następującymi polami:
    * nazwa klubu,
    * liczba punktów zdobytymi przez klub,
  Pola w tym formularzu powinny być wypełnione danymi pobranymi z bazy danych (inputy powinny mieć wypełniony atrybut `value`). Pamiętaj o tym żeby nie dać możliwości zmiany ID klubu!
* dane prześle metodą POST na ten sam adres,
* przy wejściu metodą POST odbierze dane, sprawdzi czy liczby są poprawne i zmodyfikuje wpis dotyczący klubu w bazie danych. 

<!-- Links -->
[degrees-convertion]:https://pl.wikipedia.org/wiki/Skala_Fahrenheita#Spos.C3.B3b_dok.C5.82adny
