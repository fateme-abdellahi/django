from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    password2=forms.CharField()
    class Meta:
        model=User
        fields=["username","email","password",]
        
    def clean_password2(self):
        data=super().clean()
        if data.get("password")!=data.get("password2"):
            raise forms.ValidationError("passwords aren't the same")
        return data