from .models import Places
from django.forms import ModelForm, TextInput


class PlacesForm(ModelForm):
    class Meta:
        model = Places
        fields = ['title', 'comment']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название места'
            }),
            "comment": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Комментарий'
            }),
        }
