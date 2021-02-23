from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'



class UploadForm(forms.Form):

    ONE = 'one'
    TWO = 'two'
    THREE = 'three'

    CONTENT_CHOICES = ((ONE, 'one'), (TWO, 'two'), (THREE, 'three'),)

    name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    var = forms.ChoiceField(choices=CONTENT_CHOICES)


class NewUploadForm(UploadForm):

    TWO = 'two'
    FOUR = 'four'

    CONTENT_CHOICES = ((TWO, 'two'), (FOUR, 'four'),)

    city = forms.CharField(max_length=50)
    var = forms.ChoiceField(choices=CONTENT_CHOICES)
