from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    password2=forms.CharField()
    class Meta:
        model=User
        fields=["username","email","password",]
        
    def save(self, commit=True):
        user=super().save(commit=False)
        user.username=self.cleaned_data['username']
        user.set_password(self.cleaned_data['password'])
        user.email=self.cleaned_data['email']
        
        if commit:
            user.save()
            
        return user
    
    def clean_password(self):
        data = self.cleaned_data["password"]
        if len(data)<8:
            raise forms.ValidationError("password length cannot be less than 8")
        return data
    
    
    def clean_password2(self):
        data=super().clean()
        if data.get("password")!=data.get("password2"):
            raise forms.ValidationError("passwords aren't the same")
        return data