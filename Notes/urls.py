from .views import *
from django.urls import path


urlpatterns = [
    path('<int:pk>/',notecc, name='notecc'),
    path('Note_Etudiant',etudiant, name='etudiant'),
    path('Etudiant',netudiant, name='netudiant'),
    path('classe_etudiant',classe, name='classe'),
    path('classe',nclasse, name='nclasse'),
    path('inscription_prof',inscription_prof, name='inscription_prof'),
] 