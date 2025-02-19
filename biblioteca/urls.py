from django.urls import path
from . import views

# namespace para urls
# evita conflito de nomes
# permite usar urls do tipo 'app_name:name'
# Ex. 'biblioteca:index'
app_name="biblioteca"
urlpatterns = [
    path("", views.index, name="index"),
]
