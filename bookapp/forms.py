from django import forms
from bookapp.models import Books

class BookCreateForm(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    author=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    price=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))
    publisher=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

class BookChangeForm(forms.ModelForm):
    class Meta:
        model=Books
        fields=["name","author","price","publisher"]
        
