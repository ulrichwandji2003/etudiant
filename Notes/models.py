from django.db import models

class Classe(models.Model):
    nom_classe = models.CharField(max_length=100, verbose_name="Nom de la Classe")
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
    description = models.TextField(blank=True, null=True, verbose_name="Description")

    def __str__(self):
        return f"{self.nom_classe} ({self.niveau})"


class Etudiant(models.Model):
    GENRE_CHOICES = [
        ('M', 'Masculin'),
        ('F', 'Féminin'),
    ]

    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100, blank=True, null=True)
    date_naissance = models.DateField()
    lieu_naissance = models.CharField(max_length=150)
    genre = models.CharField(max_length=1, choices=GENRE_CHOICES)
    nom_classe = models.ForeignKey(Classe, on_delete=models.CASCADE, related_name="etudiants",null=True,blank=True )
    matricule = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.nom} {self.prenom} ({self.matricule})"
  