# Team Management App

## Overview

Team Management App is a Django web application designed for managing team members. It allows users to add, edit, delete, and list team members with their details such as name, role, email, and phone number.

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Virtual environment (recommended)
- Django 4.2.7

## Setting Up the Development Environment

### Clone the Repository

```sh
git clone https://github.com/<your-username>/<team-member-management>.git
cd <team-member-management>
```

### Create and Activate a Virtual Environment

For Unix and MacOS:

```sh
python3 -m venv venv
source venv/bin/activate
```

For Windows:

```sh
python -m venv venv
.\venv\Scripts\activate
```

### Install Dependencies

```sh
pip3 install -r requirements.txt
```

### Database Migration

Apply the migrations to create the database schema:

```sh
python manage.py migrate
```

## Running the Project

### Development Server

Start the development server with:

```sh
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`
