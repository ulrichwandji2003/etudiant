from django.shortcuts import render,redirect,get_object_or_404
from django.http import JsonResponse
from .models import *
from django.contrib import messages

# Create your views here.
def notecc(request,pk):

    classe = get_object_or_404(Classe,pk=pk)
    etudiant = Etudiant.objects.filter(nom_classe=classe)
    context = {
        'classe': classe,
        "etudiant": etudiant,
        }
    
    
    return render(request, 'Note/notecc.html',context)

def etudiant(request):

    if request.method == 'POST':
        data = request.POST
        noms = data.getlist('nom[]')
        prenoms = data.getlist('prenom[]')
        dates = data.getlist('date[]')
        lieus = data.getlist('lieu[]')
        genres = data.getlist('genre[]')
        classes = data.getlist('classe[]')
        matricules = data.getlist('matricule[]')

        for i in range(len(noms)):
            Etudiant.objects.create(
                nom=noms[i],
                prenom=prenoms[i],
                date_naissance=dates[i],
                lieu_naissance=lieus[i],
                genre=genres[i],
                classe=classes[i],
                matricule=matricules[i]
            )

        return JsonResponse({'message': 'Étudiants enregistrés avec succès !'})
    
    return render(request, 'Note/etudiants.html')


def netudiant(request):

    n = Etudiant.objects.all()
    context = {
        'n': n,

        }
    
    
    return render(request, 'Note/netudiant.html',context)


def classe(request):

    n = Classe.objects.all()
    context = {
        "n" : n,
    }
    
    
    return render(request, 'Note/classe.html',context)


def inscription_prof(request):


    if request.method == 'POST':
        data = request.POST
        noms = data.getlist('nom[]')
        prenoms = data.getlist('prenom[]')
        dates = data.getlist('date[]')
        lieus = data.getlist('lieu[]')
        genres = data.getlist('genre[]')
        classes = data.getlist('classe[]')
        matricules = data.getlist('matricule[]')

        for i in range(len(noms)):
            Etudiant.objects.create(
                nom=noms[i],
                prenom=prenoms[i],
                date_naissance=dates[i],
                lieu_naissance=lieus[i],
                genre=genres[i],
                classe=classes[i],
                matricule=matricules[i]
            )

        return JsonResponse({'message': 'Étudiants enregistrés avec succès !'})
    
    return render(request, 'couverture/inscription_prof.html')



def nclasse(request):

    if request.method == 'POST':
        nom_classe = request.POST.get('nom_classe')
        niveau = request.POST.get('niveau')
        description = request.POST.get('description')

        if nom_classe and niveau:
            Classe.objects.create(nom_classe=nom_classe, niveau=niveau, description=description)
            messages.success(request, "Classe enregistrée avec succès !")
        else:
            messages.error(request, "Veuillez remplir tous les champs.")

    return render(request, 'Classe/nclasse.html')