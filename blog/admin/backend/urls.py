from django.urls import path
from .views import views
from .views import auth


urlpatterns = [
    path('', views.index, name='admin'),
    path('login/', auth.login, name='login'),
]