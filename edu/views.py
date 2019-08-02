from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def show_number(request, number):
    answer = """
             <html>
              <body>
               <p>The answer is %s!</p>
              </body>
             </html>
             """ % number
    return HttpResponse(answer)
