from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import ArticleModel
from .forms import EditForm

# Create your views here.

@login_required
def index(request):
    return render(request,"blog/index.html",{"articles":ArticleModel.objects.all()})

@login_required
def article(request,id):
    article=get_object_or_404(ArticleModel,id=id)
    return render(request,"blog/article.html",{"article":article})

@login_required
def admin_index(request):
    return render(request,"blog/admin/index.html",{"articles":ArticleModel.objects.all()})

@login_required
def admin_article_delete(request,id):
    article=get_object_or_404(ArticleModel,id=id)
    article.delete()
    return HttpResponseRedirect("/admin")

@login_required
def admin_article_edit(request,id):
    article=get_object_or_404(ArticleModel,id=id)
    if request.method=="POST":
        form=EditForm(request.POST,instance=article)
        if form.is_valid():
            form.save()
        return render(request,"blog/admin/edit-article.html",{"article":article,"errors":form.errors})

    return render(request,"blog/admin/edit-article.html",{"article":article})

@login_required
def admin_article_create(request):
    if request.method=="POST":
        form=EditForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request,"blog/admin/create-article.html",{"errors":form.errors})

    return render(request,"blog/admin/create-article.html")
