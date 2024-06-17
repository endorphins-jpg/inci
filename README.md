<h1 align="center">Desafio Técnico - Desenvolvimento Full Stack Jr</h1>
<h2 align="center">INCI Brasil</h2>

```
git clone https://github.com/endorphins-jpg/inci.git
```


<h3 align="center">Sumário</h3>

* [Tecnologias utilizadas](#tecnologias-utilizadas)
* [Instalação:](#instalação)
    * [Ambiente virtual:](#1-ambiente-virtual)
        * [Linux](#linux)
        * [Windows](#windows)
    * [Banco de dados:](#2-banco-de-dados)
        * [Criação de usuários](#criação-de-usuários) 
    * [Iniciando o projeto](#3-iniciando-o-projeto)
* [Rotas:](#rotas)
    * [POST](#post)
    * [GET](#get)

# Tecnologias utilizadas:

* [Django](https://docs.djangoproject.com/) (5.0.6)
* [jQuery](https://blog.jquery.com/) (3.6.4)
* [Bootstrap](https://getbootstrap.com/) (5.3)
* [Material Design](https://m3.material.io/)


# Instalação:

## 1. Ambiente virtual:

#### Linux:

```
sudo apt install virtualenv

virtualenv nome_da_venv

source nome_da_env/bin/activate

python3 -m pip install Django==5.0.6
```

#### Windows:

```
pip install virtualenv

virtualenv nome_da_venv

nome_da_env\Scripts\activate.ps1

python -m pip install Django==5.0.6
```

## 2. Banco de dados:
```
python/python3 manage.py migrate

manage.py loaddata fixture.json
```
#### Criação de usuários:
```
python manage.py shell
from django.contrib.auth.models import User
user = User.objects.create_user('usuario', password = 'senha') 
user.save()
```
### 3. Iniciando o projeto:

```
python/python3 manage.py runserver
```

# Rotas:

## POST:

### /api/user-plataforma/

#### Parâmetros da Requisição

* **user_id** (integer, obrigatório): O ID do usuário que será associado à plataforma.

* **plataforma_id** (integer, obrigatório): O ID da plataforma à qual o usuário será associado.

#### Resposta:

* **201 Created**.

```
{
  "message": "Plataforma adicionada ao usuario com sucesso."
}
```

### /api/user-ferramenta/

#### Parâmetros da Requisição

* **user_id** (integer, obrigatório): O ID do usuário que será associado à plataforma.

* **ferramenta_id** (integer, obrigatório): O ID da ferramenta à qual o usuário será associado.

#### Resposta:

* **201 Created**.

```
{
  "message": "Ferramenta adicionada ao usuario com sucesso."
}
```

## GET:

### /plataformas/

#### Parâmetros da Requisição

* Não requer parâmetros adicionais na URL ou no corpo da requisição, utiliza o usuário atualmente autenticado para filtrar as plataformas.

#### Resposta:

Retorna um array JSON com objetos representando cada plataforma associada ao usuário autenticado. Cada objeto contém os seguintes campos:

* **nome** (string): O nome da plataforma.
* **link** (string): Um link associado à plataforma.

**Exemplo:**

```
[
  {
    "nome": "Plataforma A",
    "link": "https://link-a.com"
  },
  {
    "nome": "Plataforma B",
    "link": "https://link-b.com"
  }
]
```

### /ferramentas/

#### Parâmetros da Requisição

* Não requer parâmetros adicionais na URL ou no corpo da requisição, utiliza o usuário atualmente autenticado para filtrar as ferramentas.

#### Resposta:

Retorna um array JSON com objetos representando cada ferramenta associada ao usuário autenticado. Cada objeto contém os seguintes campos:

* **nome** (string): O nome da ferramenta.
* **link** (string): Um link associado à ferramenta.

**Exemplo:**

```
[
  {
    "nome": "Ferramenta A",
    "link": "https://link-a.com"
  },
  {
    "nome": "Ferramenta B",
    "link": "https://link-b.com"
  }
]
```