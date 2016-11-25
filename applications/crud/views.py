from django.shortcuts import render
from applications.crud.models import Cars


def index(request):
    cars = Cars.objects.all()
    context = {
        'cars': cars
    }
    return render(request, 'index.html', context)