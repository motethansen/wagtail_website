# Creating a website with Wagtail

Wagtail was derived from the Django framework, and still work very well together.
Setting of a website with Wagtail is slightly different from Django.

For this we start very simply by creating the virtual environment

```shell
python3.11 -m venv .venv

source .venv/bin/activate
```

once the virtual environment is setup, install the django package

```shell
pip install --upgrade pip
pip install wagtail
```

Create a project folder:

```
mkdir wagtail_website
cd wagtail_website
```

Run wagtail start with an additional argument to specify the destination directory

```
wagtail start mysite wagtail_website
```

This will use the folder wagtail_website and create the files that the solution uses.
You will notice that the structure and some of the files are similar to Django.

```
wagtail_website/
├── .dockerignore
├── Dockerfile
├── home/
├── manage.py*
├── mysite/
├── requirements.txt
└── search/
```

edit the requirements.txt and add python-dotenv

```
Django>=5.1,<5.2
wagtail>=6.4,<6.5
python-dotenv==0.19.1
```

then run the pip install
```
pip install -r requirements.txt
```

### Create the database
By default, your database is SQLite. To match your database tables with your project’s models, run the following command:
```
python manage.py migrate
```

This command ensures that the tables in your database match the models in your project. Every time you alter your model, then you must run the python manage.py migrate command to update the database. For example, if you add a field to a model, then you must run the command.

---
## The Makefile

under home, I added management and commands folders, and in them are the files createsuperuserauto.py and deletesuperuser.py
They use the .env file in the root folder
```
wagtail_website\
    .env
```

inside the file are the super user credentials

```
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_PASSWORD=securepassword123
DJANGO_SUPERUSER_EMAIL=admin@example.com
```

**You will have to create this file in your project, as it does not get committed to git.**

now use the makefile to migrate the database

```
make migration
```

check the help from the makefile

```
make help
```

Output:
```
Available commands:
  make migrate          - Run Django migrations
  make createsuperuser  - Create superuser from .env file if it doesn’t exist
  make deletesuperuser  - Delete superuser specified in .env file
  make run              - Run the Django development server
```

to Build all:

```
make build
```
This executes:

pip install -r requirements.txt (installs dependencies)
python manage.py makemigrations (generates migration files)
python manage.py migrate (applies migrations)
python manage.py collectstatic — noinput (collects static files)
Use this when setting up the project for the first time or after updating requirements.txt.

## Setting Up a Superuser

Using the makefile you can create the superuser like this:

```
make createsuperuser
```

This runs python manage.py createsuperuserauto to create the superuser if it doesn’t exist. Use this after setting up the database.

To delete a superuser use make deletesuperuser:

```
make deletesuperuser
```

