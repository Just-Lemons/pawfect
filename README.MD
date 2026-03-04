In Linux

In windows --- powershell(as adminstrator)
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

Step 1 : Create Virtual Environments
-- or use pip(easier)

python3 -m venv env
source venv/bin/activate

Step 2 : Install Django

pip install django
pip freeze

step 3:create projrct

django-admin startproject [project name] 
django-admin startproject [project name] .

step 4:create app 
django-admin startapp [app name]


asgi - asynchronous  server gate way interface
wsgi - web server gate way interface

Models
1.python manage.py makemigrations
2.python manage.py migrate

