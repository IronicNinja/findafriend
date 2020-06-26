from django import forms
from django.contrib.auth.models import User

GENDER_CHOICES = [
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other')
]

MY_CHOICES = (('item_key1', 'Item title 1.1'),
              ('item_key2', 'Item title 1.2'),
              ('item_key3', 'Item title 1.3'),
              ('item_key4', 'Item title 1.4'),
              ('item_key5', 'Item title 1.5'))

class UserQuestionForm(forms.Form):
    name = forms.CharField()
    age = forms.DecimalField()
    gender = forms.CharField(widget=forms.Select(choices=GENDER_CHOICES))
    country = forms.CharField()
    interests = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=MY_CHOICES)


