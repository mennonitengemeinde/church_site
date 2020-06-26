# Church Site

- [Church Site](#church-site)
  - [Dev Stack](#dev-stack)
  - [Setup Dev enviroment](#setup-dev-enviroment)
    - [Windows](#windows)
      - [Clone the repo to you computer.](#clone-the-repo-to-you-computer)
      - [Setup enviroment variables](#setup-enviroment-variables)
      - [Create virtual enviroment](#create-virtual-enviroment)
      - [Install dependencies](#install-dependencies)
      - [Setup Database](#setup-database)
      - [Run Django](#run-django)

## Dev Stack
- Django
- Postgresql
- Sendgrid - for Email
- Azure Blob storage - for storing sermons

## Setup Dev enviroment

### Windows

Make sure you have the following installed
- Python 3
- npm
- Postgresql

#### Clone the repo to you computer.

#### Setup enviroment variables
Create a copy of the "env.example" file and name it ".env"

Make sure you have the following variables.
- DEBUG
  - off=False and on=True - If you are developing then set to on
- DB_USER
- DB_PASSWORD
- DB_HOST

Delete the variables you dont want to use.

#### Create virtual enviroment
In terminal run the following command. This will create a virtual enviroment a folder named venv where it will install the packages for this project.

```
python -m venv venv
```

To activate the virtual enviroment run:
```
.\venv\Scripts\activate
```

To deactivate the virtual enviroment run:
```
deactivate
```

#### Install dependencies
Make sure you activated the python virtual enviroment.
If you see (venv) then your good to continue.

Install python packages:
```
python -m pip install -r requirements.txt
```

Install npm modules:
```
npm install
```

#### Setup Database
Make sure you did the following
1. Make sure you have Postgresql installed
2. Create a database named "church_db"
3. Have python virtual env activated

Run migrations and create a super user
```
python manage.py migrate

python manage.py createsuperuser
```

If you want to add some sample data run:
```
python manage.py addsampledata
```

#### Run Django
To run django run:
```
python manage.py runserver
```

At this point you can navigate with a web browser to the following: http://127.0.0.1:8000

