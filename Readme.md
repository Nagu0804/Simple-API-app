# Project Name
A simple api for recording attendances and employee details.

## Table of Contents

- [Overview](#overview)
- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Authentication and Authorization](#authentication-and-authorization)


## Overview

Provide an introduction to your project, its purpose, and any key features.

## Getting Started

### Prerequisites

- Python (>=3.6)
- pip (Python package manager)

### Installation

1. Create and activate a virtual environment (recommended):


python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate


2. Install project dependencies:


pip install -r requirements.txt


3. Run migrations:


python manage.py makemigrations
python manage.py migrate


4. Create Super User:


python manage.py createsuperuser


5. Start the development server:


python manage.py runserver


## Usage
Explain how to use your application. Provide examples of making API requests and receiving responses.

## API Endpoints
Document your API endpoints and their functionalities here.

For example:

users/: List of users.

users/<int:pk>/: User details.

attendance/: List of attendances

attendance/<int:pk>: employee details

employees/: List of employees

employees/<int:pk>: employees details

## Authentication and Authorization
Authentication is set up for JWT authentication, Session authentication and Basic authentication
