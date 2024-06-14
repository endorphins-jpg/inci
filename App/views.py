from django.shortcuts import render
from .models import *
from .forms import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
# from django.shortcuts import render, get_object_or_404, redirect

def index(request):
    return render(request, 'index.html')

# @login_required
def hub(request):
    return render(request, 'hub.html')

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# ==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==

def create_plataformas(request):
    if request.method == 'POST':
        form = PlataformaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse({'message': 'ok'})
    else:
        form = PlataformaForm()
    return render(request, 'form.html', {'form': form})

def create_ferramentas(request):
    if request.method == 'POST':
        form = FerramentaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse({'message': 'ok'})
    else:
        form = FerramentaForm()
    return render(request, 'form.html', {'form': form})

# ==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==

def get_plataformas(request):
    plataformas = list(Plataforma.objects.all().values('nome', 'link'))
    return JsonResponse(plataformas, safe = False)

def get_ferramentas(request):
    ferramentas = list(Ferramenta.objects.all().values('nome', 'link'))
    return JsonResponse(ferramentas, safe = False)