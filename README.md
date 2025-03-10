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

then collect the package names in a requirements file

```shell
pip freeze > requirements.txt
```

