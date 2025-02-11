# Ingest AI Email Outreach Service

## Overview
This project is a **Lead Verification & Email Outreach API** built with **Django** and **Django REST Framework (DRF)**. It allows users to:
- **Create leads** (individually or in bulk via CSV upload)
- **Authenticate & Authorize** using JWT
- **Scrape website content** for leads using **BeautifulSoup**
- **Analyze website content** and store a summary
- **Generate personalized email outreach messages** using **Anthropic AI API**
- **Send emails** using SMTP
- **Ensure users can only see and manage their own leads**

## Features
✅ **User authentication with JWT (login, token refresh)**  
✅ **Create leads (single and bulk CSV upload)**  
✅ **Extract website content (title, meta description, first paragraphs, or headings)**  
✅ **Analyze lead website using BeautifulSoup and Anthropic AI**  
✅ **Generate outreach emails using Anthropic AI API**  
✅ **Send emails via SMTP**  
✅ **User-based data access control**  
✅ **REST API with secure endpoints**  

## Tech Stack
- **Backend:** Django, Django REST Framework (DRF)
- **AI Integration:** Anthropic AI API
- **Web Scraping:** BeautifulSoup
- **Authentication:** JWT (djangorestframework-simplejwt)
- **Email Sending:** SMTP
- **Database:** SQLite3 (default), supports PostgreSQL/MySQL

## Installation

### 1. Clone the Repository
```sh
git clone https://github.com/pallab-nandi/ingest.git
cd ingest
```

### 2. Create Virtual Environment & Install Dependencies
```sh
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

### 3. Set Up Environment Variables
Create a `.env` file in the project root and add:
```ini
# Django Secret Key (use a long, random string)
SECRET_KEY=your_django_secret_key

# Anthropic API Configuration
ANTHROPIC_API_KEY=your_anthropic_api_key

# Database Configuration (optional for SQLite)
DATABASE_URL=database_url

# Debug Mode (set to False in production)
DEBUG=True

# Allowed Hosts (comma-separated for production)
ALLOWED_HOSTS=localhost,127.0.0.1

# Email Configuration (if using SMTP)
EMAIL_HOST=smtp.example.com
EMAIL_PORT=587
EMAIL_HOST_USER=your_email@example.com
EMAIL_HOST_PASSWORD=your_email_password
EMAIL_USE_TLS=True
```

### 4. Apply Migrations & Run Server
```sh
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Running Tests
```sh
python manage.py test
```
---
<br>


# Ingest Backend API



<!--- If we have only one group/collection, then no need for the "ungrouped" heading -->



## Endpoints

* [Auth](#auth)
    1. [register](#1-register)
    1. [login](#2-login)
* [LeadAPI](#leadapi)
    1. [fetchLeads](#1-fetchleads)
    1. [addLeads](#2-addleads)
    1. [bulkLeadsAdd](#3-bulkleadsadd)
    1. [fetchLeadById](#4-fetchleadbyid)
    1. [leadScrape](#5-leadscrape)
    1. [leadAiAnalyze](#6-leadaianalyze)
    1. [generateEmail](#7-generateemail)

--------



## Auth



### 1. register



***Endpoint:***

```bash
Method: POST
Type: RAW
URL: {{localhost}}/api/v1/register
```



***Body:***

```js        
{
    "username": "parry",
    "email": "parry@platypus.com",
    "password": "parrytheplatipus",
    "confirm_password": "parrytheplatipus"
}
```



### 2. login



***Endpoint:***

```bash
Method: POST
Type: RAW
URL: {{localhost}}/api/v1/login
```



***Body:***

```js        
{
    "username": "tim",
    "password": "timcook"
}
```



## LeadAPI



### 1. fetchLeads



***Endpoint:***

```bash
Method: GET
Type: 
URL: {{localhost}}/api/v1/leads
```



### 2. addLeads



***Endpoint:***

```bash
Method: POST
Type: RAW
URL: {{localhost}}/api/v1/leads
```



***Body:***

```js        
{
    "name": "Django Project",
    "email": "djangoproject@gmail.com",
    "website_url": "https://www.djangoproject.com/"
}
```



### 3. bulkLeadsAdd



***Endpoint:***

```bash
Method: POST
Type: FORMDATA
URL: {{localhost}}/api/v1/leads/bulk
```



***Body:***

| Key | Value | Description |
| --- | ------|-------------|
| file |  |  |



### 4. fetchLeadById



***Endpoint:***

```bash
Method: GET
Type: 
URL: {{localhost}}/api/v1/leads/2
```



### 5. leadScrape



***Endpoint:***

```bash
Method: PUT
Type: RAW
URL: {{localhost}}/api/v1/leads/1/scrape
```



***Body:***

```js        
{
    "name": "Django Project",
    "email": "djangoproject@gmail.com",
    "website_url": "https://www.djangoproject.com/"
}
```



### 6. leadAiAnalyze



***Endpoint:***

```bash
Method: PUT
Type: RAW
URL: {{localhost}}/api/v1/leads/1/analyze
```



***Body:***

```js        
{
    "name": "Django Project",
    "email": "djangoproject@gmail.com",
    "website_url": "https://www.djangoproject.com/"
}
```



### 7. generateEmail



***Endpoint:***

```bash
Method: PUT
Type: RAW
URL: {{localhost}}/api/v1/leads/1/generate_email
```



***Body:***

```js        
{
    "name": "Django Project",
    "email": "djangoproject@gmail.com",
    "website_url": "https://www.djangoproject.com/"
}
```



---
[Back to top](#ingest-backend-api)
