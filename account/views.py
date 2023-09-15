from django.contrib.auth import get_user_model, login, logout, authenticate
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Visit
from datetime import date


# Create your views here.
User = get_user_model()

def liste_utilisateurs(request):
    utilisateurs = User.objects.all()
    data = [{'username': user.username, 'email': user.email, 'first_name': user.first_name, 'last_name': user.last_name} for user in utilisateurs]
    return JsonResponse(data, safe=False)

def visites(request):
    try:
        # Récupérer ou créer un objet Visit correspondant à la date actuelle
        today = date.today()
        visit, created = Visit.objects.get_or_create(date=today)

        # Renvoyer la date et le nombre de visites correspondant à cette date
        return JsonResponse({'Date': today.strftime('%Y-%m-%d'), 'Nombre de visites': visit.count})
    except Visit.DoesNotExist:
        return JsonResponse({'message': 'Le nombre de visites n\'existe pas'}, status=404)

def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
        login(request, user)
        return redirect('index')
    return render(request, 'account/signup.html')

def logout_user(request):
    logout(request)
    return redirect('index')

def login_user(request):
    if request.method == "POST":
        #Connecter user
        username = request.POST.get("username")
        password = request.POST.get("password")
        # on check avec user dans la BD
        user = authenticate(username=username, password=password)
        if user:
            increment_visit_count()
            login(request, user)
            return redirect('index')
    return render(request, 'account/login.html')


def increment_visit_count():
    # Récupérer l'objet Visit (compteur de visites) ou le créer s'il n'existe pas encore
    today = date.today()
    print("incrementer!!!")
    visit, created = Visit.objects.get_or_create(date=today)

    # Incrémenter le compteur de visites
    visit.count += 1
    visit.save()