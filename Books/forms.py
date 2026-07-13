from .models import Book
from django import forms 

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre']

    title = forms.CharField(widget=forms.TextInput(attrs={'class':'inp mb-4'}))
    author = forms.CharField(widget=forms.TextInput(attrs={'class':'inp mb-4'}))
    genre = forms.CharField(widget=forms.TextInput(attrs={'class':'inp mb-4', 'placeholder':'Genres (e.g Mystery, Suspense)'}))
