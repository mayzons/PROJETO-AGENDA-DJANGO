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
