# ERP

This is a simple ERP. The ideia is create an ERP where you can change and customize according to your needs.

---

# Tecnologies

- Python
- Django
- Django Rest Framework
- Docker

---

# Structure Project

- setup
    - *.py
- templates
    - *.html
    - *.js
- static
    - *.css
    - *.js
    - *.html
    - *.png
    - *.jpg

---

# Start Here

### 1. Create a virtual enviroment:

```powershell
python -m venv .venv
```

### 2. Active your venv:

Windows:
```powershell
.venv\Scripts\activate
```

Linux or MacOS:
```powershell
source .venv/bin/activate
```

### 3. Install requirements.txt:

```powershell
pip install -r requirements.txt
```

---

#  Starting the project with Docker
 
### Buildind the image Docker

```shell
    docker build -t soft .
```
<br>

### Starting the container

```shell
    docker run -p 8000:8000 soft
```

<br>

---

## Starting locally

### Install the dependencies:

```shell
    pip install -r requirements.txt
```

<br>

### Run migrate:


```shell
    python manage.py migrate
```

<br>

### Create a super user:

```shell
    python manage.py createsuperuser
```
<br>

### Starting the server:

```shell
    python manage.py runserver
```

Acesse: [localhost:8000/admin](localhost:8000/admin)

<br>