from django import forms

class Add_to_Cart(forms.Form):
    item=forms.IntegerField()
    user=forms.IntegerField()
    size=forms.CharField()

