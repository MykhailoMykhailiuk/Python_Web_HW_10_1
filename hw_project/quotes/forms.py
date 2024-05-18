from django import forms
from .models import Author, Quote, Tag


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['full_name', 'born_date', 'born_location', 'description']


class QuoteForm(forms.ModelForm):
    author = forms.ModelChoiceField(
        queryset=Author.objects.all(), 
        required=False, 
        widget=forms.Select()
    )
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(), 
        required=False, 
        widget=forms.SelectMultiple()
    )

    class Meta:
        model = Quote
        fields = ['quote', 'author', 'tags']

