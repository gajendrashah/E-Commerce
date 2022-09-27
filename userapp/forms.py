from pyexpat import model
from django.forms import ModelForm


from .models import Customers


class customercretionform(ModelForm):
    class Meta:
        model = Customers
        fields = '__all__'