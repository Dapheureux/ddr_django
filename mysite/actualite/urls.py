from django.urls import path

from . import views
urlpatterns = [
    path('actualite', view=views.actualite, name="actualite"),
]
