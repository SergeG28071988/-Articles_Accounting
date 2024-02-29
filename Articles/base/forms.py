from django import forms
from .models import *


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('last_name', 'first_name', 'date_of_birth')


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'content', 'date_published', 'author')