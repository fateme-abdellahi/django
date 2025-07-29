from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('article/<int:id>',views.article,name="view-article"),
    path('admin/<int:id>/delete',views.admin_article_delete,name="admin-article-delete"),
    path('admin/<int:id>/edit',views.admin_article_edit,name="admin-article-edit"),
    path('admin/create',views.admin_article_create,name="admin-article-create"),
    path('admin/',views.admin_index,name="admin-page"),
]