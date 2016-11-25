from django.forms import ModelForm

from applications.crud.models import Cars


class AddCarForm(ModelForm):
    class Meta:
        model = Cars
        exclude = ['id']