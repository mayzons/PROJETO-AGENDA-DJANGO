# Ambinetes
python -m venv venv
. venv/bin/activate

# -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------

# DJANGO
Iniciar o projeto Django

pip install django
django-admin startproject project .
python manage.py startapp nameapp

# Migrações de projeto (MIGRATION)
python manage.py makemigrations
python manage.py migrate

# Criando usuário e senha do console Admin

python manage.py createsuperuser            --> Pedira user, e-mail e senha do superuser
python manage.py changepassword NOMEUSER            --> Caso esqueca a senha do super usuário

# Ambiente server
python manage.py collectstatic

# -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------

# Trabalhando com o model do Django

# Importe o módulo
from contact.models import Contact
# Cria um contato (Lazy)
# Retorna o contato
contact = Contact(**fields)
contact.save()
# Cria um contato (Não lazy)
# Retorna o contato
contact = Contact.objects.create(**fields)
# Seleciona um contato com id 10
# Retorna o contato
contact = Contact.objects.get(pk=10)
# Edita um contato
# Retorna o contato
contact.field_name1 = 'Novo valor 1'
contact.field_name2 = 'Novo valor 2'
contact.save()
# Apaga um contato
# Depende da base de dados, geralmente retorna o número
# de valores manipulados na base de dados
contact.delete()
# Seleciona todos os contatos ordenando por id DESC
# Retorna QuerySet[]
contacts = Contact.objects.all().order_by('-id')
# Seleciona contatos usando filtros
# Retorna QuerySet[]
contacts = Contact.objects.filter(**filters).order_by('-id')


# -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------

# GIT

# Congiguração local do GIT
git config --global user.name 'Seu nome'
git config --global user.email 'seu_email@gmail.com'
git config --global init.defaultBranch main

# Configure o .gitignore
git init
git add .
git commit -m 'Mensagem'
git remote add origin URL_DO_GIT

# Para ver o commit
git log 
git log --oneline
git status 

# Para fazer o push a primeira vez
git push origin main -u

>> Próximas vezes
git commit -m 'Mensagem'
git push
