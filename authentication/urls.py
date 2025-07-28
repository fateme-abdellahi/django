from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.urls import reverse_lazy

urlpatterns = [
    path('register/',views.register,name="register"),
    path('login/',views.Login.as_view(),name="login"),
    path('logout/',auth_views.LogoutView.as_view(next_page=reverse_lazy('login')),name="logout"),
    # path('logout/',auth_views.LogoutView.as_view(next_page='login'),name="logout"),
    # path('logout/',auth_views.LogoutView.as_view(),name="logout"),
]