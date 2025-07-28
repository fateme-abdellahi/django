from django import forms
from .models import ArticleModel

class EditForm(forms.ModelForm):
    class Meta:
        model=ArticleModel
        fields="__all__"