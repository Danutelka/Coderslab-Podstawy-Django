from django.shortcuts import render
from django.http import HttpResponse
from random import randint

# Create your views here.

def show_number(request, number):
    answer = """
             <html>
              <body>
               <p>The answer is %s!</p>
              </body>
             </html>
             """ % number
    return HttpResponse(answer)

def hello(request):
    return HttpResponse("Hello world!")

def random1(request):
    los = randint(0,101)
    tekst = """
        <html>
        <body>
            <p>Wylosowano liczbę %s!</p>
              </body>
             </html>
             """ % los
    return HttpResponse(tekst)

def random_max(request, number):
    los2 = randint(0, number)
    tekst2 = """
        <html>
        <body>
            <p>Użytkownik podał wartość: %s. Wylosowano liczbę: %s</p>
         </body>
        </html>""" % (number,los2)
    return HttpResponse(tekst2)

def random_max_min(request, min_number, max_number):
    los3 = randint(min_number, max_number)
    tekst2 = """
        <html>
        <body>
            <p>Użytkownik podał wartośći %s i %s.</p>
            <p>Wylosowano liczbę: %s </p>
         </body>
        </html>""" % (min_number,max_number, los3)
    return HttpResponse(tekst2)

def hello_user(request, name):
    tekst3 = """
        <html>
        <body>
            <p>Hello %s </p>
         </body>
        </html>""" % name
    return HttpResponse(tekst3)
