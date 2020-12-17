from .models import Places
from django.forms import ModelForm, TextInput, DateTimeInput

class PlacesForm(ModelForm):
    class Meta:
        model = Places
        fields = ['title','comment','date']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название места'
            }),
            "comment": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Комментарий'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder':'Дата публикации'
            })
        }