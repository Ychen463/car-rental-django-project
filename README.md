# Car Rental Platform

Welcome to the Car Rental Platform, a robust and user-friendly web application built with Django and PostgreSQL. Our platform offers a seamless car rental experience, featuring advanced search and filtering, role-based user permissions, social authentication, and an integrated messaging system.

## Table of Contents

- [Car Rental Platform](#car-rental-platform)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Technology Stack](#technology-stack)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)

## Features

- **Advanced Search and Filtering**: Easily find the perfect car with our advanced search and filtering options.
- **Role-Based User Permissions**: Securely manage access with distinct roles for administrators, renters, and car owners.
- **Social Authentication**: Sign in quickly and securely using your social media accounts.
- **Integrated Messaging**: Communicate seamlessly within the platform for inquiries and support.
- **Responsive Design**: Enjoy a great user experience on any device.

## Technology Stack

- **Backend**: Django, Python
- **Database**: PostgreSQL
- **Frontend**: HTML, CSS, JavaScript (Django Templates)
- **Authentication**: Django Allauth
- **Text Editor**: CKEditor
- **Deployment**: Gunicorn, Whitenoise

## Getting Started

### Prerequisites

- Python 3.8 or later
- pip (Python package installer)
- Virtualenv (optional, for isolated Python environments)

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/car-rental-platform.git
   cd car-rental-platform

2. ** Set Up a Virtual Environment (Optional) **
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. Install Dependencies
    ```bash
    pip install -r requirements.txt
### Configuration
1. Environment Variables
Create a .env file in the project directory and add your configuration:
``` 
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=postgres://user:password@localhost/dbname
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY=your_google_oauth2_key
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET=your_google_oauth2_secret

```
Replace the placeholders with your actual data.

2. Database Migrations
```
python manage.py migrate
```
3. Create a Superuser (Optional)

```
python manage.py createsuperuser
```