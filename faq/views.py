### faq app views


from django.shortcuts import render
from django.http import HttpResponse

def list(request):
    return HttpResponse("hi there")
