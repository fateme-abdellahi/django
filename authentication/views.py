from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import RegisterForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
# Create your views here.
def register(request):
    if request.method=="GET":
        form=RegisterForm()
        return render(request,"registration/register.html")
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            if User.objects.filter(email=form.data.get("email")).exists():
                return render(request,"registration/register.html",{"email_exists":True})
            user=form.save()
            login(request,user)
            return redirect('index')
        return render(request,"registration/register.html",{"errors":form.errors})

class Login(LoginView):
    redirect_authenticated_user=True
    def get_success_url(self):
        return reverse('index')
    