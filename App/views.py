from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')

@login_required
def hub(request):
    return render(request, 'hub.html')

def login_view(request): 
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return HttpResponseRedirect('/hub/')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

# ==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==

def get_plataformas(request):
    usuario = request.user
    plataformas = list(Plataforma.objects.filter(usuarios = usuario).values('nome', 'link'))
    return JsonResponse(plataformas, safe = False)

def get_ferramentas(request):
    usuario = request.user
    ferramentas = list(Ferramenta.objects.filter(usuarios = usuario).values('nome', 'link'))
    return JsonResponse(ferramentas, safe = False)

# ==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==

@csrf_exempt
def link_user_plat(request):
    try:
        user_id = request.POST.get('user_id')
        plataforma_id = request.POST.get('plataforma_id')

        user = get_object_or_404(User, id=user_id)
        plataforma = get_object_or_404(Plataforma, id = plataforma_id)

        plataforma.usuarios.add(user)
        plataforma.save()

        return JsonResponse({'message': 'Plataforma adicionada ao usuario com sucesso.'}, status=201)

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

        return JsonResponse({'message': 'Ferramenta adicionada ao usuario com sucesso.'}, status=201)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status = 400)