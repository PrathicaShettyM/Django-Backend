# Django-Backend
This is a popular python web framework for rapidly building web applications

## Table of Contents
- [First time Installation](#first-time-installation)
- [Subsequent running](#to-run-subsequent-timesafter-restarting-the-system)
- [Django architecture](#django-architecture)
- [Setting up Static and Template folders](#setting-up-static-and-template-folders-for-use)
- [Tailwind CSS with Django](#tailwindcss-with-django)
- [Django Templates]()


## First-time Installation
We need `uv` package manager
1. Set a virtual environment for the django project with the command(open bash)
```
uv venv
```
2. Activate the virtual environment
```
source .venv/Scripts/activate
```
3. If you face any error in Windows OS, open the `windows-powershell` as an `administrator` and type the following command
```
set-exectionpolicy remotesigned
```
4. Install Django with the command
```
uv pip install Django
```
5. Create a new Django project
```
django-admin startproject MyApp
```
6. Come inside the project folder
```
cd MyApp
```
7. Run the Django server
```
python manage.py runserver 
```
- Use the above command whenever you want to restart the server(Dont forget to navigate to the manage.py's directory)

- If some the port is blocked for some reason then use a port number
```
python manage.py runserver 8001
```


## To run subsequent times(After restarting the system)
You will need to use the following commands 
```
source .venv/Scripts/activate

cd MyApp

python manage.py runserver
```
- Note: If you are not restarting the system, then use `py manage.py runserver` command

# Django Architecture

1. A project with the desired name is created, along a subfolder with the same name which contains - 
`views.py`: contains the core functionalities of the application(contains logic)
`urls.py`: contains all routes
`settings.py`: contains all settings

2. `db.sqlite3` is a default database for django which can also be migrated to `postgres` and `mysql`

3. `manage.py` is the starting point of the application. It is the server

4. `static folder` contains `css` and `js` files

5. `templates folder` contains `html` files 


## Setting up static and template folders for use

1. change this in `settings.py` to load `css` and `js` files
```
STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
```

2. In `index.html` do the following changes
```
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MyApp | Django project</title>
    <link rel="stylesheet" href="{% static 'style.css' %}">
</head>
<body>
    <h1>This is a Django project</h1>
    
</body>
</html>
```

3. In `views.py` do the following to render the html file on the browser
```
def home(request):
    return render(request, 'website/index.html')
```

## TailwindCSS with Django
1. Install `pip` and then `tailwind css`
- Whichever the below command works use it
- command 1
```
py -m ensurepip --upgrade
```
- command 2
```
py -m pip install --upgrade pip
```

```
pip install django-tailwind
```
Note: use both when needed

2. Install `tailwind css` with the following command
```
pip install 'django-tailwind[reload]'
```
3. Go to `settings.py` and in apps object, add 'tailwind'

4. Use this command to initiate tailwind in the server. Some packages will be installed along with a folder named `theme` if you keep the default settings
- Go to `settings.py` and in apps object, add 'theme'
```
py manage.py tailwind init
```
5. Go to `settings.py` and add 'theme' in the app section
6. Next below it give the name of the tailwind app and `InternalIP`
```
TAILWIND_APP_NAME = 'theme'
INTERNAL_IPS = ['127.0.0.1']
NPM_BIN_PATH = 'C:/Program Files/nodejs/npm.cmd'
```
7. Use the command 
```
python manage.py tailwind install
```
8. Inject the tailwind commands from the base.hmtl of `theme` folder into layout.html file in MyApp
```
{% load static tailwind_tags %}

{% tailwind_css %}
```
9. Open one more terminal(it also has to be bash) and name it `tailwind` and run this command
```
 python manage.py tailwind start
```
10. In the normal terminal where the django app is running, restart the server over there. Now tailwind starts generating css

11. Do the following in `settings.py` to enable hot reloading
```
MIDDLEWARE = [
    "django_browser_reload.middleware.BrowserReloadMiddleware"
]

INSTALLED_APPS = [
    "chai",
    "tailwind",
    "theme",
    "django_browser_reload"
]
```

12. Do this in `views.py` of MyApp
```
urlpatterns = [

    path("__reload__/", include("django_browser_reload.urls")), 
]

```

## super user and admin
1. Due migrations get migrated. After this command we wont get the inital erros
```
python manage.py migrate
```


## Jinja2 and Django apps

1. Create a new project in the folder
```
python manage.py startapp chai
```

2. Go to settings add emmet for django-html

3. Create layouts and inject code
```
{% extends "layout.html" %}

{% block title %}
    all chai page | index.html title
{% endblock %}

{% block content %}
    <h1>Which chai would u like to have ? </h1>
{% endblock %}
```

