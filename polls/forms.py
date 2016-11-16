from django import forms

class PostForm(forms.Form):
    # question1 = forms.IntegerField(required=True)
    for i in range(1,201):
        globals()['question{0}'.format(i)] = forms.IntegerField(required=True)