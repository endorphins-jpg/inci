from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

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

def get_plataformas(request):
    usuario = request.user
    plataformas = list(Plataforma.objects.filter(usuarios = usuario).values('nome', 'link'))
    return JsonResponse(plataformas, safe = False)

def get_ferramentas(request):
    usuario = request.user
    ferramentas = list(Ferramenta.objects.filter(usuarios = usuario).values('nome', 'link'))
    return JsonResponse(ferramentas, safe = False)

@csrf_exempt
def link_user_plat(request):
    try:
        user_id = request.POST.get('user_id')
        plataforma_id = request.POST.get('plataforma_id')

        user = get_object_or_404(User, id=user_id)
        plataforma = get_object_or_404(Plataforma, id = plataforma_id)

        plataforma.usuarios.add(user)
        plataforma.save()

        return JsonResponse({'message': 'Plataforma adicionada ao usuário com sucesso.'}, status=201)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status = 400)

@csrf_exempt
def link_user_ferr(request):
    try:
        user_id = request.POST.get('user_id')
        ferramenta_id = request.POST.get('ferramenta_id')

        user = get_object_or_404(User, id=user_id)
        ferramenta = get_object_or_404(Ferramenta, id=ferramenta_id)

        ferramenta.usuarios.add(user) 
        ferramenta.save()

        return JsonResponse({'message': 'Ferramenta adicionada ao usuário com sucesso.'}, status=201)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status = 400)