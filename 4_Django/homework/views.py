from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from homework.models import Person
from homework.models import Genre
from homework.models import Movie
from homework.models import PersonMovie
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def movies(request):
    movies_list = Movie.objects.order_by('-id')
    response = HttpResponse()
    for el in movies_list:
        response.write(
            "<p><a href='/movie_detail/{id}'>{title}</a> {year} {director} {genre}</p>" .format(id=el.id, title=el.title, year=el.year, director=el.director, genre=",".join(g.name for g in el.genre.all()))
            )
    return response

def movie_detail(request, id):
    movie = Movie.objects.get(id=id)
    html = """
        <h1>{title}</h1>
        <h2>{director}</h2>
        <h3>{genre}</h3>
        """ .format(title=movie.title, director=movie.director, genre=",".join(g.name for g in movie.genre.all()))
    return HttpResponse(html)
"""
filtr zwraca liste w nawiasie (id=id)
def movie_detail(request, movie_id):
    filmy1 = Movie.objects.filter(pk=movie_id)
    detail = '<ul>'
    for y in filmy1:
        detail += "<li> Tytuł: {title} </li>" .format(title=y.title)
        detail += "<li> Starring: {starring} </li>"  .format(starring=y.starring)
        detail += "<li> Rok produkcji: {year} </li>" .format(year=y.year) 
        detail += "<li> Rating: {rating} </li>" .format(rating=y.rating)
        detail += "<li> Gatunek: {genre} </li>" .format(genre=y.genre)
    detail += '</ul>'
    return HttpResponse(detail)
"""
def all_persons(request):
    person_list = Person.objects.order_by('-id')
    response = HttpResponse()
    for el in person_list:
        response.write(
            "<p> {first_name} <a href='/person_detail/{id}'>{last_name}</a></p>" .format(id=el.id, first_name=el.first_name, last_name=el.last_name)
            )
    return response

def person_detail(request, id):
    person = Person.objects.get(id=id)
    html = """
        <h1>{first_name}</h1>
        <h2>{last_name}</h2>
        <p><a href="/person_edit/{id}">Edytuj</a></p>
        <p><a href="/persons">lista ludzi</a></p>
        """ .format(first_name=person.first_name, last_name=person.last_name, id=person.id)
    html += '<p><a href="/add">Dodaj osobe</a>'
    return HttpResponse(html)

@csrf_exempt
def person_add(request):
    form = """
        <form method="POST">
            <label>imie:
            <input type="text" name="first_name">
            </label>
            <label>Nazwisko:
            <input type="text" name="last_name">
            </label>
            <input type="submit"value="Dodaj">
        """
    if request.method =='POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        nowa = Person.objects.create(first_name=first_name, last_name=last_name, id=10)
        return redirect('person_detail/{id}'.format(id=nowa.id))
    else:
        return HttpResponse(form)

@csrf_exempt
def person_edit(request, id):
    p = Person.objects.get(id=id)
    form = """
        <form method="POST">
            <label>imie:
            <input type="text" name="first_name" value="{first_name}">
            </label>
            <label>Nazwisko:
            <input type="text" name="last_name" value="{last_name}">
            </label>
            <input type="submit"value="Dodaj">
        """ .format(first_name=p.first_name, last_name=p.last_name)
    if request.method =='POST':
        p.first_name = request.POST.get('first_name')
        p.last_name = request.POST.get('last_name')
        p.save()
        return redirect('person_detail/{id}'.format(id=nowa.id))
    else: #obsluga metody GET
        return HttpResponse(form)

def search_movie(request):
    form = """
        <form>
            <label> Tytuł: <input type="text" name="title"></label>
            <input type="submit" value="szukaj">
        </form>
        """
    title = request.GET.get('title')
    response = HttpResponse(form)
    if title is not None:
        m = Movie.objects.filter(title__icontains=title)
        response.write('<h2>Wyniki</h2>')
        for movie in m:
            response.write('<p><a href="/movie_detail/{movie.id}">{movie.title}</a></p>' .format(movie=movie)
            )
    return response


"""    
def all_persons(request):
    osoby = Person.objects.all()
    opis = '<ul>'
    for w in osoby:
        opis += "<li> Imię: {first_name} Nazwisko: {last_name}</li>" .format(first_name=w.first_name, last_name=w.last_name)
    opis += '</ul>'
    return HttpResponse(opis)
"""
"""
def edit_person(request, person_id):
    osoba = Person.objects.filter(pk=person_id)
    opis2 = '<ul>'
    for x in osoba:
        opis2 += "<li> Id: {id}</li>" .format(id=x.id)
        opis2 += "<li> Imię: {first_name}" .format(first_name=x.first_name)
        opis2 += "<li> Nazwisko: {last_name} </li>" .format(last_name=x.last_name)
    opis2 += '</ul>'
    return HttpResponse(opis2)

def edit_person2(request, first_name, last_name):
    imie = Person.objects.get(fist_name=first_name)
    nazwisko = Person.objects.get(last_name=last_name)
    if request.method == 'POST'
    
    opis2 = 
            <form> 
                <labeL>
                Podaj imie: 
                <input
            </form>
    
    opis2 += '</ul>'
    return HttpResponse(opis2)
"""