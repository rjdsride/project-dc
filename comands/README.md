INICIANDO PROJETO
python -m venv venv
. venv/bin/activate
pip install django
django-admin startproject project .
python manage.py startapp project


-- UPANDO PRO GITHUB --
git config --global user.name 'name'
git config --global user.email 'email
git config --global init.defaultBranch main
# Configure o .gitignore
git init
git add .
git commit -m 'Mensagem'
git remote add origin url


-- ALTERANDO A BASE DE DADOS --
python manage.py makemigrations
python manage.py migrate

--CRIANDO SUPER USER --
python manage.py createsuperuser
python manage.py changepassword USERNAME