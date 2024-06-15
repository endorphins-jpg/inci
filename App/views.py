from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, get_object_or_404

def index(request):
    if request.user.is_authenticated:
        return render(request, 'hub.html')
    else:
        return render(request, 'index.html')

def login_view(request): 
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

# ==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==

def create_plataformas(request):
    if request.method == 'POST':
        form = PlataformaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse({'message': 'ok'})

def create_ferramentas(request):
    if request.method == 'POST':
        form = FerramentaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse({'message': 'ok'})
        
# ==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==

def edit_plataforma(request, pk):
    plataforma = get_object_or_404(Plataforma, pk = pk)
    if request.method == 'POST':
        form = PlataformaForm(request.POST, instance = plataforma)
        if form.is_valid():
            form.save()
            return HttpResponse({'message': 'ok'})
    else:
        form = PlataformaForm(instance = plataforma)
    return render(request, 'form.html', {'form': form})

# ==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==

def get_plataformas(request):
    usuario = request.user
    plataformas = list(Plataforma.objects.filter(usuarios = usuario).values('nome', 'link'))
    return JsonResponse(plataformas, safe = False)

def get_ferramentas(request):
    ferramentas = list(Ferramenta.objects.all().values('nome', 'link'))
    return JsonResponse(ferramentas, safe = False)