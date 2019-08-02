from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from exercises.models import Article
from exercises.models import Band
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def show_article(request, id):
    a = Article.objects.get(id=id)
    html = """
        <h1>{category}</h1>
        <h2>{title}</h2>
        <h3>{author}</h3>
        <h4>{content}</h4>
        <h5>{date_added}></h5>
        <h6>{status}</h6>
        """ .format(category=a.category, 
                    title=a.title, author=a.author, 
                    content=a.content, date_added=a.date_added, status=a.status)
    return HttpResponse(html)

def show_band(request, id):
    b = Band.objects.all()
    html = '<ul>'
    for y in b:
        html += "<li> {id} {name} {genre} {year} {still_active}" .format(id=y.id, name=y.name, genre=y.genre, year=y.year, still_active=y.still_active)
    html += '</ul>'
    return HttpResponse(html)


# zad1 dzien3
def range_view(request):
    start = request.GET.get('start')
    end = request.GET.get('end')
    html = "<html><body>"
    html += """
            <form>
            <input name="start">
            <input name="end">
            <button type="submit">wyślij</button>
            </form>
            """
    if start and end:
        for x in range(int(start), int(end)+1):
            html += "%d" % x
    else:
        html += "<p>brak informacji, wpisz odpowiednie wartosci</p>"
    html += "</body></html>"

    return HttpResponse(html)

#zad2 dzien 3

def tabliczka_mnozenia_view(request):
    width = request.GET.get('height')
    height = request.GET.get('width')
    html = "<html><body>"
    html += """
            <form>
            <label>wyskosc: <input name=height></label>
            <label>szerokosc:<input name="width"></label>
            <button type="submit">wyślij</button>
            </form>
            """
    if height and width:
        html += "<table>"
        for y in range(1, int(height)+1):
            html += "<tr>"
            for x in range(1, int(width) + 1):
                html += "<td>{v}</td>".format(v=x*y)
            html += "</tr>"
        html += "</table>"
    else:
        html += "<p>brak informacji, wpisz odpowiednie wartosci</p>"
    html += "</body></html>"

    return HttpResponse(html)

# dzien 3 zad 2/1
@csrf_exempt
def witaj(request):
    html = ""
    if request.method == "GET":
        html += "<p>Wypełnij!</p>"
    elif request.method == "POST":
        imie = request.POST.get('imie')
        nazwisko = request.POST.get('nazwisko')
        html += "<p> Witaj {imie} {nazwisko} </p>" .format(imie=imie, nazwisko=nazwisko)
    
    html += """
        <form method="POST">
        <label>imie: <input name=imie></label>
        <label>nazwisko:<input name="nazwisko"></label>
        <button type="submit">wyślij</button>
        </form>
            """
    return HttpResponse(html)

# dzien 3 zad 2/2
@csrf_exempt
def temperatura(request):
    html = ""
    if request.method == "GET":
        html += "<p>Ile stopni?</p>"
        html += """
        <form action="" method="POST">
        <label>
            Temperatura:
        <input type="number" min="0.00" step="0.01" name="degrees">
        </label>
        <input type="submit" name="convertionType" value="celcToFahr">
        <input type="submit" name="convertionType" value="FahrToCelc">
        </form>
        """
    elif request.method == "POST":
        convertionType = request.POST.get('convertionType')
        degrees = float(request.POST.get('degrees'))
        if convertionType == 'celcToFahr':
            fahr = 9.0 / 5.0 * degrees +32.00
            html += "stopnie c to f: %.2f" % fahr
        elif convertionType == 'FahrToCelc':
            celc = (degrees - 32.00) * 5.0 / 9.0
            html += f"stopnie f to c: {celc}"   
    return HttpResponse(html)

#dzien 3 sesje zad1

def setSession(request):
    request.session['counter'] = 0
    return HttpResponse("")

def showSession(request):
    counter = request.session.get('counter')
    if counter is not None:
        html = "<p>counter = {} </p>" .format(counter)
        counter = counter +1
        request.session['counter'] = counter
        return HttpResponse(html)
    else: 
        return HttpResponse("Brak countera")

def delSession(request):
    if request.session.has_key('counter'):
        del request.session['counter']
        return HttpResponse("klucz został usunięty")
    else:
        return HttpResponse("klucz nie istnieje")

#dzien 3 sesje zad2

def login(request):
    if request.method == 'POST':
        imie = request.POST.get('name')
        request.session['loggedUser'] = imie
    else:
        imie = request.session.get('loggedUser')
        if imie:
            return HttpResponse("Witaj, {}" .format(imie))
    return render(request, "templates.html")

#dzien 3 sesje zad3

def addToSession(request):
    if request.method == 'POST':
        key = request.POST.get('key')
        value = request.POST.get('value')
        request.session[key]= value
    return render(request, "form2.html")

def showAllSession(request):
    context = {
        'session': request.session.items() # lista kluczy i wartości
    }
    return render(request, "tabelka.html", context=context)


# cookies 1

def setCookie(request):
    response = HttpResponse()
    response.set_cookie('user', 'danka')
    return response

def showCookie(request):
    imie = request.COOKIES.get('user')
    if imie is not None:
        html = '''<p>{}</p>''' .format(imie)
        return HttpResponse(html)
    else: 
        return HttpResponse("Bbrak imienia")

def delCookie(request):
    response = HttpResponse()
    if 'user' in request.COOKIES:
        response.delete_cookie('user')
        return response
    else:
        return HttpResponse("klucz nie istnieje")

# zad 2 cookies

def addToCookie(request):
    if request.method == 'POST':
        response = HttpResponse() # pusty response
        key = request.POST.get('key') # input name=key
        value = request.POST.get('value') # input name=value
        response.set_cookie(key, value) #ustawiamy ciasteczko
        return response # wysylamy odp do uztkownika z nowym ciasteczkiem
    return render(request, "form3.html")

def showAllCookies(request):
    context = {
        'cookies': request.COOKIES.items()
    }
    return render(request, "tabelka2.html", context=context)