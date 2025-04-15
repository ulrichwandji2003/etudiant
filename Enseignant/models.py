from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Enseignant(models.Model):
    GENRE_CHOICES = [
        ('M', 'Masculin'),
        ('F', 'Féminin'),
    ]
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    nom_prenom = models.CharField(max_length=255,blank=False)
    utilisateur = models.CharField(max_length=255,blank=False)
    genre = models.CharField(max_length=1, choices=GENRE_CHOICES, default="M")
    mot_passe = models.CharField(max_length=255,blank=False)
    date_naiss = models.DateField(max_length=255,blank=False)
    matricule = models.CharField(max_length=200, blank=False,default='')
    telephone = models.CharField(max_length=200, blank=False,default='')
    email =models.EmailField()
    matiere = models.CharField(max_length=30,blank=False)
    niveau = models.CharField(
        max_length=50,
        choices=[
            ('Niveau-1', 'Niveau-1'),
            ('Niveau-2', 'Niveau-2'),
            ('Niveau-3', 'Niveau-3'),
            ('Niveau-4', 'Niveau-4'),
            ('Niveau-5', 'Niveau-5'),
            ('Niveau-6', 'Niveau-6'),
        ],
        verbose_name="Niveau"
    )

    def __str__(self):
        return self.nom_prenom