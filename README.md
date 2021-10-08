# PCS3643 - Laboratório de Engenharia de Software

O projeto da disciplina é um sistema para leilões online.

## Aulas 2,3 e 4

As entregas das aulas 2,3 e 4 podem ser encontradas em suas respectivas pastas.

## Implementação do Projeto

A partir da aula 5, o projeto começou a ser implementado no framework **Django**.

O propósito da versão atual do projeto é implementar funcionalidade **CRUD** para as classes **leiloeiro, comprador e vendedor** todas munidas de atributos **nome, cpf e bio**.

## Criação de Ambiente Virtual pipenv

Para criar e iniciar ambiente virtual com **pipenv**

> pipenv install django

> pipenv shell

## Boas práticas

Importante usar `{% csrf_token %}` para todo formulário Django.

Foram adicionados métodos `get_absolute_url()` e `__str()__` para todos os models.

## Banco de dados sqlite

Para criar banco de dados inicial sqlite

> python manage.py migrate

Sempre que um novo Model é criado, precisamos atualizar o Django em dois passos.

> python manage.py makemigrations

> python manage.py migrate

## Criando superuser

Para interagir com banco de dados na página **admin** foi criado um superuser com o comando

> winpty python manage.py createsuperuser

### Credenciais

Usuário: ArkhamKnightGPC

Senha: password

## Executando app

Para executar servidor Django

> python manage.py runserver

Então basta acessar o endereço **http://127.0.0.1:8000/**

Para sair do ambiente virtual basta digitar 

> exit
