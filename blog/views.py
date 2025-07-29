from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required, user_passes_test
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


def is_staff_member(user):
    return user.is_staff

@user_passes_test(is_staff_member)
def admin_index(request):
    return render(request,"blog/admin/index.html",{"articles":ArticleModel.objects.all()})

@user_passes_test(is_staff_member)
def admin_article_delete(request,id):
    article=get_object_or_404(ArticleModel,id=id)
    article.delete()
    return HttpResponseRedirect(reverse('admin-page'))

@user_passes_test(is_staff_member)
def admin_article_edit(request,id):
    article=get_object_or_404(ArticleModel,id=id)
    if request.method=="POST":
        form=EditForm(request.POST,instance=article)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin-page'))
        return render(request,"blog/admin/edit-article.html",{"article":article,"errors":form.errors})

    return render(request,"blog/admin/edit-article.html",{"article":article})

@user_passes_test(is_staff_member)
def admin_article_create(request):
    if request.method=="POST":
        form=EditForm(request.POST)
        if form.is_valid():
            title=form.data.get('title')
            if ArticleModel.objects.filter(title=title).exists():
                form.add_error('title','an article with this title already exists')
                return render(request,"blog/admin/create-article.html",{"errors":form.errors})
            form.save()
            return HttpResponseRedirect(reverse('admin-page'))
        return render(request,"blog/admin/create-article.html",{"errors":form.errors})

    return render(request,"blog/admin/create-article.html")
