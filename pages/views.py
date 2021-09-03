from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs): # *args, **kwargs
  print(request.user)
  print(args, kwargs)
  #return HttpResponse("<h1>Hello World</h1>") # string of HTML code
  return render(request, "home.html", {})

def contact_view(request, *args, **kwargs): # *args, **kwargs
  print(request.user)
  print(args, kwargs)
  #return HttpResponse("<h1>Hello World</h1>") # string of HTML code
  return render(request, "contact.html", {})

def about_view(request, *args, **kwargs): # *args, **kwargs
  my_context = {
    "my_text": "This is about me",
    "my_number": 123,
    "my_list": [123, 4242, 12314]
  }
  #return HttpResponse("<h1>Hello World</h1>") # string of HTML code
  return render(request, "about.html", my_context)