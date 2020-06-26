from django import forms
from django.contrib.auth.models import User

class UserQuestionForm(forms.Form):
    name = forms.CharField()
    age = forms.DecimalField()
    country = forms.CharField()
    country1 = forms.CharField()
    country2 = forms.CharField()
    country3 = forms.CharField()
    country4 = forms.CharField()
    country5 = forms.CharField()
