# PCS3643 - Laboratório de Engenharia de Software

O projeto da disciplina é um sistema para leilões online. Estamos em fase de implementação.

## Versão atual do Projeto

É possível cadastrar dois tipos de usuários com permissões diferentes dentro do site: **Leiloeiro** e Clientes (**Compradores** e **Vendedores**).

> Após cadastro, um email personalizado é enviado confirmando o cadastro. A conta gratuita do **Twilio SendGrid** oferece até 100 emails por dia, o que é suficiente para nossos propósitos.

O pacote **django-bootstrap4** foi usado para embelezar o projeto.

## Como rodar localmente ?

### Banco de dados local

O projeto utiliza um banco MySQL local com as seguintes especificações **settings.py**. Portanto é necessário criar esse database localmente.

>DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'projetoleilaopcs3643',
        'USER': 'nameuser',
        'PASSWORD': 'pass',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

### Subindo servidor Django

Primeiramente é necessário instalar o **pipenv**

> pip install env

Então na pasta **ProjetoLeilao**, ativar o ambiente virtual

> pipenv shell

E executar

>python manage.py runserver

## Referências e recursos importantes

- Livro **Django for Beginners, William S. Vincent**

- [Customizing User Authentication in Django](https://docs.djangoproject.com/en/3.2/topics/auth/customizing/) 

- [Using Twilio SendGrid To Send Emails from Python Django Applications](https://www.twilio.com/blog/using-twilio-sendgrid-send-emails-python-django)

- [How to implement multiple user types with Django](https://simpleisbetterthancomplex.com/tutorial/2018/01/18/how-to-implement-multiple-user-types-with-django.html)