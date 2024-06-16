from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('login/', views.login_view, name = 'login'),
    path('logout/', views.logout_view, name = 'logout'),

    path('create_ferramenta/', views.create_ferramentas, name = 'create_ferramentas'),
    path('create_plataforma/', views.create_plataformas, name = 'create_plataformas'),

    path('edit_plataforma/<int:pk>/', views.edit_plataforma, name = 'edit_plataforma'),
    
    path('plataformas/', views.get_plataformas, name = 'get_plataformas'),
    path('ferramentas/', views.get_ferramentas, name = 'get_ferramentas')
    ]
