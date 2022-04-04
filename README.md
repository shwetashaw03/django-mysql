# Make Virtual Environment
```cmd
python -m venv <name>
```

# Activate Virtual Environment
```cmd
source <name>/Scripts/activate
```

# Dependency List to Requirements.txt
```cmd
pip freeze > requirements.txt
```

# Install all dependency from Requirements.txt
```cmd
pip install -r requirements.txt
```

# Uninstall all dependency using Requirements.txt
```cmd
pip uninstall -r requirements.txt
```

- - -

# Django Setup
- After creating virtual environment, activate it
- Install django
```cmd
pip install django
```
- Start django Project
```py
# Way1
django-admin startproject main_app

# Way2 in current directory
django-admin startproject main_app .
```
- Running server
```py
#default: http://127.0.0.1:8000/
py manage.py runserver

#At specified port: http://127.0.0.1:8080/
py manage.py runserver 8080
```
- Creating App
```cmd
py manage.py startapp blogs
```

- Register app to the `settings.py` file of main projects
```py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #my app
    'blogs',
]
```

# Integrating Django and XAMPP MySQL
- Run xampp Server
- Create Database
- Install MySQL Client in python 
```cmd
pip install mysqlclient
```
- Configure database in the `settings.py` file of main projects
```py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': <Database_name>,
        'USER':'root',
        'PASSWORD':'',
        'HOST':'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'sql_mode': 'traditional',
        }
    }
}
```
- Migrating the database
```py
py manage.py makemigrations
py manage.py migrate
```

- Empting All the Data
```py
py manage.py flush
```

- To remove all migrations
```txt
1) Go inside app (blogs)
2) Go to migrations
3) Except __init.py__ delete all files
4) Also remove the __pycache__ directory completely
```

- - -

# Creating SuperUser
```py
py manage.py createsuperuser
```

- - -

# Register to Admin
- Adding the model of app to the admin via `admin.py`
```py
from django.contrib import admin
from .models import Social

# Register your models here.
class SocialAdmin(admin.ModelAdmin):
    fields = ['site', ('link', 'active'), 'icon']
    list_display = ['site', 'active']


admin.site.register(Social,SocialAdmin)
```

- - -

# App Config
- Like changing the app name in admin
```py
from django.apps import AppConfig

class SeoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'seo'
    verbose_name = "SEO Optimization"
```

- - -

# Static Files
```py
python manage.py collectstatic
```

- - -

# Add templates
- Create templates
```py
mkdir templates
cd templates
touch home.html
```

- Configure setting in `settings.py`
```py
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```