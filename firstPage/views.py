from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

# GET your views here.
def firstPage(request):
    return render(request, "firstPage.html")
