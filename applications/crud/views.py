from django.shortcuts import render
from applications.crud.models import Cars


def index(request):
    cars = Cars.objects.all()
    context = {
        'cars': cars
    }
    return render(request, 'index.html', context)

def car_detail(request, pk):
    try:
        car = Cars.objects.get(pk=pk)
    except:
        car = None

    context = {
        'car': car
    }
    return render(request, 'car_details.html', context)
