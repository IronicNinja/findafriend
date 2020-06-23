from django import forms
from django.contrib.auth.models import User

class UserQuestionForm(forms.Form):
    name = forms.CharField()
    age = forms.DecimalField()
    country = forms.CharField()