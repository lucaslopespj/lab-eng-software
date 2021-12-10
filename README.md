# PCS3643 - Laboratório de Engenharia de Software

O projeto da disciplina é um sistema para leilões online. O deploy foi feito utilizando **Heroku** e pode ser acessado no link [https://projetoleilao.herokuapp.com/](https://projetoleilao.herokuapp.com/)

Com o objetivo de facilitar testes da versão local do projeto, trocamos o banco de dados MySQL usado ao longo da disciplina por SQLite. A versão para deploy no **Heroku** utiliza um banco de dados Postgres.

## Documentação do Projeto e Slides da Apresentação

A documentação do projeto desenvolvido ao longo do curso se encontra na pasta **Documentação**.

Os slides utilizados na apresentação final também estão na pasta **Documentação**

## Como rodar localmente ?

Primeiramente, é necessário ter o **pipenv**. ![Como baixar pipenv ?](https://pypi.org/project/pipenv/)

Agora, com o pipenv, vamos instalar **requirements.txt**

> pipenv install -r requirements.txt

Então para ativar o ambiente virtual

> pipenv shell

Realizar as migrações para deixar seu banco igual o nosso

> python manage.py migrate

Agora basta executar o servidor

> python manage.py runserver

Observação: Caso você queira limpar o banco SQLite para fazer seus testes, use o comando 

> python manage.py flush

## Pasta Screenshots

Para esclarecer o fluxo de usuário no projeto e criar uma memória visual do projeto, adicionamos uma pasta **Screenshots** contendo capturas de tela da versão atual do projeto em funcionamento.

![Homepage](Screenshots/homepage.png)

## O que tem na versão atual do projeto ?

### Funcionalidades

- Signup de usuários Leiloeiros e Clientes

- Login e Logout de usuários

#### Para usuário cliente

- Ofertar lote de produto (vendedor paga taxa de comissão)

- Realizar lance em lote de produto (saldo de compradores e vendedores envolvidos é atualizado) 

- Atualizar saldo bancário

- Conferir saldo bancário

#### Para usuário Leiloeiro

- Gerar Relatório de Faturamento

- Gerar Relatório de Desempenho

- Liberar Lote para leilão

- Finalizar Leilão

## Referências e recursos importantes

- Livro **Django for Beginners, William S. Vincent**

- [User Authentication in Django](https://docs.djangoproject.com/en/3.2/topics/auth/)

- [How to raise form validation errors](https://docs.djangoproject.com/en/dev/topics/forms/modelforms/#overriding-the-clean-method)

- [Linking user model to a custom profile model](https://prog.world/one-to-one-relationship-linking-a-user-model-to-a-custom-profile-model-in-django/)

- [Making database queries in Django](https://docs.djangoproject.com/en/3.2/topics/db/queries/)
