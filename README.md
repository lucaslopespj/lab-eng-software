# PCS3643 - Laboratório de Engenharia de Software

O projeto da disciplina é um sistema para leilões online.

## Aulas 2,3 e 4

As entregas das aulas 2,3 e 4 podem ser encontradas em suas respectivas pastas.

## Entrega Aula 6

O propósito da versão atual do projeto é implementar models para todas as classes e relacionamentos envolvidas no diagrama ER do sistema e realizar migration para banco de dados **MySQL** local.

A entrega também inclui o diagrama entidade relacionamento do sistema.

## Criação de Ambiente Virtual pipenv

Para criar e iniciar ambiente virtual com **pipenv**

> pipenv install django

> pipenv shell

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
