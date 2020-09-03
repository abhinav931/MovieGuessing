from django.shortcuts import render
from .models import MovieNames
from random import choices
# Create your views here.
def HomePageView(request):
    return render(request, 'index.html')


def PlayPageView(request):
    obj = choices(MovieNames.objects.all())
    name, length = obj[0].movieName, len(obj[0].movieName)
    context = {'name': name, 'length': length}
    return render(request, 'play.html', context)