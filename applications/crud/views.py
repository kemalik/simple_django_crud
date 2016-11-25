from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from applications.crud.models import Cars
from applications.crud.forms import AddCarForm

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


def add_car(request):
    form = AddCarForm(request.POST, request.FILES)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    context = {
        'form': form
    }

    return render(request, 'add_car.html', context)