# PCS3643 - Laboratório de Engenharia de Software

O projeto da disciplina é um sistema para leilões online.

## Banco de dados

O pacote pymsql, listado em **requirements.txt**, foi utilizado para conexão com banco de dados MySQL local. Sempre que um novo Model é criado, precisamos atualizar o Django em dois passos.

> python manage.py makemigrations

> python manage.py migrate

É necessário também modificar **settings.py** do app Django porque o banco padrão é sqlite3.

`DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Grupo2LabEngSoft',
        'USER': 'nameuser',
        'PASSWORD': 'pass',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}`

## Aulas 2,3 e 4

As entregas das aulas 2,3 e 4 podem ser encontradas em suas respectivas pastas.

## Entrega Aula 6

O propósito da versão atual do projeto é implementar models para todas as classes e relacionamentos envolvidas no diagrama ER do sistema e realizar migration para banco de dados **MySQL** local.

A entrega também inclui o diagrama entidade relacionamento do sistema.

## Entrega Aula 7

### Caminho de navegação desenvolvido

Durante a aula 7, implementamos as templates **html** e **css** correspondentes para cobrir o seguinte caminho de navegação:

- Usuário Vendedor com intenção de Ofertar um lote de produtos acessa a página inicial http://127.0.0.1:8000/

- Usuário clica no link **Deseja ofertar um lote ?**

- Usuário é redirecionado automaticamente para http://127.0.0.1:8000/lote/new

- Usuário preenche o formulário com dados do Lote e aperta botão **Save**

- Usuário é automaticamente redirecionado para página inicial http://127.0.0.1:8000/

- Para conferir que seu lote foi cadastrado, Usuário clica no link **Veja nossos lotes de Produtos!**

- Usuário vê seu lote cadastrado e fecha a aba do navegador satisfeito.

### Templates associadas a funções CRUD

As templates **comprador_home.html**, **comprador_new.html**, **comprador_edit.html**, **comprador_detail.html**, **comprador_delete.html** estão associadas as funções CRUD do model Comprador.

As templates **leiloeiro_home.html**, **leiloeiro_new.html**, **leiloeiro_edit.html**, **leiloeiro_detail.html**, **leiloeiro_delete.html** estão associadas as funções CRUD do model Leiloeiro.

As templates **vendedor_home.html**, **vendedor_new.html**, **vendedor_edit.html**, **vendedor_detail.html**, **vendedor_delete.html** estão associadas as funções CRUD do model Vendedor.

As templates **formulario_ofertar_novo_lote.html**, **lote_home.html**, **lote_edit.html**, **lote_detail.html**, **lote_delete.html** estão associadas as funções CRUD do model Lote. Note que a template **formulario_ofertar_novo_lote.html** pertence ao caso de uso ***Ofertar Lotes de Produtos***.

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

## Executando app

Para executar servidor Django

> python manage.py runserver

Então basta acessar o endereço **http://127.0.0.1:8000/**

Para sair do ambiente virtual basta digitar 

> exit

## Referências

- Livro Django for Beginners, William S. Vincent. Temos um repositório com projetos correspondentes aos capítulos do livro https://github.com/ArkhamKnightGPC/TreinandoDjango
