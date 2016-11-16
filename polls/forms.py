from django import forms

class PostForm(forms.Form):
    question1 = forms.IntegerField(required=True)
    question2 = forms.IntegerField(required=True)