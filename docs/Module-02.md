# Module 02 - Project Configuration

## Module Information

- **Module Number:** 02
- **Module Name:** Project Configuration
- **Status:** In Progress

Module 02 Status
Phase	Status
Phase 1 – Templates Configuration	✅ Completed
Phase 2 – Static Files Configuration	✅ Completed
Phase 3 – Media Files Configuration	✅ Completed
Phase 4 – MySQL Configuration	✅ Completed
Phase 5 – Final Testing	✅ Completed
Phase 6 – Documentation	✅ Completed
Phase 7 – Git Commit & Push	✅ Completed

---

## Objective

Configure the Django project for a scalable and production-ready structure.

---

## Goals

- Configure Templates
- Configure Static Files
- Configure Media Files
- Configure MySQL
- Verify Project Settings

---

## Current Progress

- [ ] Templates
- [ ] Static
- [ ] Media
- [ ] MySQL
- [ ] Testing

---

## Learning Outcome

Understand how Django manages templates, static files, media files, and database configuration.

## 🎓 Interview Note (Module 02 - Part 1)

Question: templates, static aur media me kya difference hota hai?

Answer:

templates/ → HTML files
static/ → CSS, JavaScript, images, fonts
media/ → User-uploaded files (profile photo, resume, project images, etc.)

Ye question Django interviews me bahut common hai.


---

## Phase 1 – Templates Configuration

### Objective

Configure Django to load templates from the project's root `templates` directory.

### File Modified

- portfolio/settings.py

### Changes Made

Updated the `DIRS` option inside the `TEMPLATES` setting.

Before:

```python
'DIRS': [],
```

After:

```python
'DIRS': [BASE_DIR / 'templates'],
```

### Why This Change?

This allows Django to load shared HTML templates from the root `templates` folder, making the project easier to organize and maintain.

### Result

The Django server runs successfully after the configuration.

### 🎤 Interview Questions
Q1. BASE_DIR kya hota hai?

Answer:
BASE_DIR project ke root folder ka path hota hai. Iska use files aur folders ke absolute paths banane ke liye hota hai.

Q2. TEMPLATES['DIRS'] ka purpose kya hai?

Answer:
Ye Django ko batata hai ki project-level templates kis folder me rakhe gaye hain.

---

## Phase 2 – Static Files Configuration

### Objective

Configure Django to serve static files from the root `static` directory.

### Folder Created

- static/
- static/css/
- static/js/
- static/images/
- static/fonts/
- static/vendor/

### File Modified

- portfolio/settings.py

### Changes Made

Added:

```python
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
```

### Why This Change?

This allows Django to load CSS, JavaScript, fonts and images from a centralized location.

### Result

Static directory configured successfully.

### Interview Questions
Q1. Static files kya hote hain?

Answer:
Static files wo files hoti hain jo change nahi hoti, jaise CSS, JavaScript, fonts aur images.

Q2. STATICFILES_DIRS ka use kya hai?

Answer:
Ye Django ko batata hai ki development ke time static files kis folder se load karni hain

---

## Phase 3 – Media Files Configuration

### Objective

Configure Django to handle user-uploaded media files.

### File Modified

- portfolio/settings.py
- portfolio/urls.py

### Changes Made

Added MEDIA_URL and MEDIA_ROOT in settings.py.

Configured media URL routing in urls.py.

### Why This Change?

Media files such as profile photos, resumes, certificates and project images will be uploaded by the administrator or user. Django needs a dedicated configuration to serve these files during development.

### Result

Media files are now configured successfully.

### Interview Questions
Q1. Difference between MEDIA_ROOT and MEDIA_URL?

Answer:

MEDIA_ROOT → Actual folder on disk where uploaded files are stored.
MEDIA_URL → URL through which browser accesses those uploaded files.
Q2. static() function ka use kyu karte hain?

Answer:

Development mode me Django automatically media files serve nahi karta. static() helper se hum media URLs ko serve karte hain jab DEBUG=True hota hai.


---

# Phase 4 – MySQL Configuration

## Objective

Replace the default SQLite database with MySQL to build a scalable and production-ready Django application.

---

## Why MySQL?

SQLite is suitable for learning and small projects, but professional web applications generally use MySQL because it offers:

- Better performance
- Multi-user support
- Improved security
- High scalability
- Better backup and recovery
- Industry-standard database management

---

## Prerequisites

Before configuring MySQL in Django, ensure that:

- MySQL Server is installed.
- MySQL Workbench or MySQL Shell is available.
- `mysqlclient` package is installed.
- A database named `dynamic_portfolio` has been created.
- Database username and password are available.

---

## Files Modified

- `portfolio/settings.py`

---

## Database Configuration

The default SQLite configuration:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

was replaced with the MySQL configuration:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dynamic_portfolio',
        'USER': 'YOUR_USERNAME',
        'PASSWORD': 'YOUR_PASSWORD',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

> **Note:** Replace `YOUR_USERNAME` and `YOUR_PASSWORD` with your actual MySQL credentials.

---

## Configuration Details

| Setting | Value |
|---------|-------|
| Database Engine | MySQL |
| Database Name | dynamic_portfolio |
| Host | localhost |
| Port | 3306 |
| Username | Your MySQL Username |

---

## Verification Steps

- Verified that MySQL Server is running.
- Verified that `mysqlclient` is installed.
- Connected Django to MySQL.
- Started the Django development server successfully.

---

## Result

The Django project is now configured to use MySQL as its primary database.

---

## Learning Outcome

After completing this phase, I learned:

- Difference between SQLite and MySQL.
- How Django connects to MySQL.
- Purpose of each key inside the `DATABASES` setting.
- Why MySQL is preferred for production applications.

---

## Common Errors

### Error

```
ModuleNotFoundError: No module named 'MySQLdb'
```

### Solution

Install mysqlclient:

```bash
pip install mysqlclient
```

---

### Error

```
Access denied for user
```

### Solution

Check the MySQL username and password.

---

### Error

```
Unknown database 'dynamic_portfolio'
```

### Solution

Create the database:

```sql
CREATE DATABASE dynamic_portfolio;
```

---

## Interview Questions

### Q1. Why is MySQL preferred over SQLite in production?

**Answer:**
MySQL provides better performance, scalability, concurrent user support, security, and backup features compared to SQLite.

---

### Q2. What is the purpose of the `DATABASES` setting in Django?

**Answer:**
The `DATABASES` setting tells Django which database engine to use and how to connect to it.

---

### Q3. What does `ENGINE` represent in the `DATABASES` setting?

**Answer:**
It specifies the database backend used by Django, such as SQLite, MySQL, or PostgreSQL.

---

## Status

☐ In Progress

---

# Phase 4 – MySQL Configuration

## Status

✅ Completed

## Objective

Configured Django to use MySQL as the primary database instead of SQLite.

---

## Files Modified

- portfolio/settings.py

---

## Database Used

- Database Engine: MySQL
- Database Name: dynamic_portfolio
- Host: localhost
- Port: 3306

---

## Changes Made

- Replaced the default SQLite configuration with MySQL.
- Configured Django database connection.
- Successfully connected the project with MySQL.
- Executed database migrations successfully.

---

## Verification

- Django connected to MySQL successfully.
- Database migrations completed successfully.
- Development server started without errors.

---

## Learning Outcome

- Learned how to configure MySQL in Django.
- Understood the purpose of the `DATABASES` setting.
- Learned the difference between SQLite and MySQL.

---

# Module 02 Summary

## Objective Achieved

Successfully configured the Django project for professional development.

## Completed Tasks

- Configured Templates directory
- Configured Static files
- Configured Media files
- Connected Django with MySQL
- Successfully executed database migrations
- Verified the Django development server

## Files Modified

- portfolio/settings.py
- portfolio/urls.py

## Skills Learned

- Django project configuration
- Template configuration
- Static files configuration
- Media files configuration
- MySQL database integration
- Django migration workflow

## Module Status

✅ Completed