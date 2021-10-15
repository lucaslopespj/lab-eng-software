# PCS3643 - Laboratório de Engenharia de Software

O projeto da disciplina é um sistema para leilões online.

## Aulas 2,3 e 4

As entregas das aulas 2,3 e 4 podem ser encontradas em suas respectivas pastas.

## Entrega Aula 6

O propósito da versão atual do projeto é implementar models para todas as classes e relacionamentos envolvidas no diagrama ER do sistema e realizar migration para banco de dados **MySQL** local.

A entrega também inclui o diagrama entidade relacionamento do sistema.

## Entrega Aula 7

A template **base.html** possui header e footer comuns para todas as nossas views.

A template **home.html** é a página inicial de nosso Diagrama de Navegação.


### Templates associadas a funções CRUD

As templates **comprador_home.html**, **comprador_new.html**, **comprador_edit.html**, **comprador_detail.html**, **comprador_delete.html** estão associadas as funções CRUD do model Comprador.

As templates **leiloeiro_home.html**, **leiloeiro_new.html**, **leiloeiro_edit.html**, **leiloeiro_detail.html**, **leiloeiro_delete.html** estão associadas as funções CRUD do model Leiloeiro.

As templates **vendedor_home.html**, **vendedor_new.html**, **vendedor_edit.html**, **vendedor_detail.html**, **vendedor_delete.html** estão associadas as funções CRUD do model Vendedor.

## Criação de Ambiente Virtual pipenv

Para criar e iniciar ambiente virtual com **pipenv**

> pipenv install django

> pipenv shell

### Versão Python

Para utilizar pipenv é necessário ter Python na versão **3.10.0**, se você possuir versão mais antiga atualize antes de usar o pipenv.

## Boas práticas

Importante usar `{% csrf_token %}` para todo formulário Django.

Foram adicionados métodos `__str()__` para todos os models.

Todas as dependências Python estão no arquivo **requirements.txt** do projeto.

## Banco de dados MySQL

Sempre que um novo Model é criado, precisamos atualizar o Django em dois passos.

> python manage.py makemigrations

> python manage.py migrate

## Executando app

Para executar servidor Django

> python manage.py runserver

Então basta acessar o endereço **http://127.0.0.1:8000/**

Para sair do ambiente virtual basta digitar 

> exit
