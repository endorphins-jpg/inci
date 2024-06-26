from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('hub/', views.hub, name = 'hub'),


    path('login/', views.login_view, name = 'login'),
    path('logout/', views.logout_view, name = 'logout'),

    # ==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==

    path('plataformas/', views.get_plataformas, name = 'get_plataformas'),
    path('ferramentas/', views.get_ferramentas, name = 'get_ferramentas'),

    # ==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==

    path('api/user-plataforma/', views.link_user_plat, name = 'link_plataforma'),
    path('api/user-ferramenta/', views.link_user_ferr, name = 'link_ferramenta'),
    ]
