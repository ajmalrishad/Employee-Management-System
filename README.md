# Employee Management System

A simple, customizable Employee Management System built with Django. This system allows admins to manage employee information, add custom fields, and view employee details. The system also includes an API for further integration.

## Features

- User authentication (login, registration, password reset)
- Employee creation, update, and deletion
- Customizable employee fields
- Dynamic Employee Detail page reflecting custom fields
- API with JWT authentication
- Responsive design with Bootstrap

## Prerequisites

- [Python 3.8+](https://www.python.org/downloads/)
- [Django 3.2+](https://www.djangoproject.com/download/)
- [MySQL Server](https://dev.mysql.com/downloads/mysql/)

## Getting Started

1. **Clone the Repository**
cmd/bash
   git clone https://github.com/ajmalrishad/Employee-Management-System.git
   cd employee-management-system
   

2. **Set Up a Virtual Environment**

   Create a virtual environment for Python dependencies:
cmd/bash
   python -m venv venv
   
   Activate the virtual environment:
   - On Windows:
  cmd/bash
     venv\Scripts\activate
     
   - On MacOS/Linux:
  cmd/bash
     source venv/bin/activate
     

3. **Install Dependencies**

   Install all necessary packages listed in `requirements.txt`:
cmd/bash
   pip install -r requirements.txt
   

4. **Set Up MySQL Database**

   Create a new database in MySQL:
   sql
   CREATE DATABASE employee_management;
   
   Update the `DATABASES` setting in `settings.py` to match your MySQL credentials:
   
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'employee_management',
           'USER': 'your_mysql_username',
           'PASSWORD': 'your_mysql_password',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }

5. **Apply Migrations**

   Run the following commands to apply migrations and set up the database schema:
cmd/bash
   python manage.py makemigrations
   python manage.py migrate
   

6. **Create a Superuser (Admin)**

   To access the Django admin dashboard, create a superuser:
cmd/bash
   python manage.py createsuperuser
   

7. **Run the Development Server**

   Start the development server:
cmd/bash
   python manage.py runserver
   
   The application will be accessible at `http://127.0.0.1:8000/`.

8. **Access the Admin Dashboard**

   Navigate to `http://127.0.0.1:8000/admin` and log in with the superuser credentials you created. You can manage employee data and customize fields directly through the admin interface or web UI.

## API Documentation

The Employee Management System includes an API for managing employee data with JWT authentication.

### Authentication

To access the API, authenticate via JWT. After logging in, obtain a token.

1. Login via the `/api/token/` endpoint to get a JWT token.
2. Use this token in the `Authorization` header for subsequent API requests.
3. use access token for api authentication

### Endpoints

#### **Employee Management**

- **GET** `/api/employees/` - Retrieve the list of employees
- **POST** `/api/v1/employees/` - Create a new employee
- **GET** `/api/v1/employees/` - Get details of all employee
- **GET** `/api/v1/employees/{id}/` - Get details of a specific employee
- **PUT** `/api/v1/employees/{id}/` - Update an employee's details
- **DELETE** `/api/v1/employees/{id}/` - Delete an employee