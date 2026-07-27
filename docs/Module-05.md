# Module 05 - Skills Module

## Module Information

- Module Number: 05
- Module Name: Skills Module
- Status: In Progress

---

## Phase 1 – Skills App Creation

### Objective

Create the Skills app and register it in the Django project.

### Files Created

- skills/

### Files Modified

- portfolio/settings.py

### Changes Made

- Created a new Django app named `skills`.
- Registered the app in `INSTALLED_APPS`.

### Result

The Skills app is successfully integrated into the project.

### Status

✅ Completed

🎤 Interview Questions
Q1. Why do we create a separate app for Skills?

Answer:
A separate app follows Django's modular architecture. It keeps related models, views, URLs, templates, and admin configuration together, making the project easier to maintain and scale.

Q2. Why must we add the app to INSTALLED_APPS?

Answer:
Django only recognizes and loads apps that are listed in INSTALLED_APPS. Without registering the app, its models, admin configuration, and migrations won't be detected.

Q3. What command creates a Django app?

Answer:

python manage.py startapp skills

# Module 05 - Skills Module

## Module Information

- Module Number: 05
- Module Name: Skills Module
- Status: In Progress

---

# Module 05 - Skills Module

## Module Information

- Module Number: 05
- Module Name: Skills Module
- Status: In Progress

---

## Phase 2 – URL Configuration

### Objective

Configure URL routing for the Skills app.

### Files Created

- skills/urls.py

### Files Modified

- portfolio/urls.py

### Result

Skills module routing configured successfully.

Status:

✅ Completed

---

## Phase 3 – Skills Model Design

### Objective

Create the Skill model to store technical skills.

### Model Fields

- name
- category
- proficiency
- icon

### Result

Skill model created successfully.

Status:

✅ Completed

---

## Phase 4 – Admin Panel Registration

### Objective

Register the Skill model in Django Admin.

### Features

- list_display
- list_filter
- search_fields

### Result

Skill model available in Django Admin.

Status:

✅ Completed

---

## Phase 5 – Database Migration

### Objective

Create the Skill table in MySQL.

### Commands Used

python manage.py makemigrations

python manage.py migrate

### Result

Skill table created successfully.

Status:

✅ Completed
🎤 Interview Questions
Q1. Why did we use choices for the category field?

Answer: It restricts the values to predefined options, improving data consistency and reducing invalid entries.

Q2. Why is proficiency a PositiveIntegerField?

Answer: Skill percentage cannot be negative, so a positive integer is appropriate.

Q3. What is the benefit of list_filter in Django Admin?

Answer: It allows filtering records based on a specific field, making data management easier.

Q4. Why do we override __str__()?

Answer: It provides a readable name for each object in the Django Admin instead of showing a generic object ID.

# Phase 6 – Skills View

## Objective

Create the first view function for the Skills page.

### Files Modified

- skills/views.py

### View Created

skills()

### Result

The Skills page view renders successfully without any errors.

Status:

✅ Completed
🎤 Interview Question
Why do we create a view before connecting the database?

Answer:

Because we first verify that the URL routing and template rendering work correctly. After that, we connect the database, making debugging easier.

# Phase 7 – Skills Template

Created the Skills page template.

Status:

✅ Completed

---

# Phase 8 – Dynamic Skills Display

Connected the Skill model with the template.

Status:

✅ Completed

---

# Phase 9 – Progress Bar Integration

Implemented Bootstrap progress bars using dynamic proficiency values.

Status:

✅ Completed

---

# Phase 10 – Skill Categories

Displayed skills based on categories using Django QuerySets.

Status:

✅ Completed
🎤 Interview Questions
Q1. Why do we pass context from the view?

To send database records from Django views to templates for rendering.

Q2. What does Skill.objects.filter() do?

It retrieves only those Skill records that match the specified condition.

Q3. Why use Bootstrap Progress Bars?

They visually represent the proficiency level of each skill.

Q4. What is the difference between all() and filter()?
all() → Returns all records.
filter() → Returns only matching records.

# Phase 11 – Final Testing

## Objective

Test the complete Skills Module.

### Testing Checklist

- Skills page opens successfully.
- Dynamic skills are displayed.
- Progress bars work correctly.
- Categories display correctly.
- Admin CRUD operations work.
- No errors in terminal.

### Result

Skills Module tested successfully.

Status:

✅ Completed

🎤 Interview Questions
Q1. Why do we test after every module?

Answer:

Testing helps identify errors early, making debugging easier and ensuring each module works independently before moving to the next.

Q2. What is CRUD?

Answer:

Create
Read
Update
Delete

These are the four basic database operations.

🎤 Interview Questions
Q1. Why should documentation be updated after every module?

Answer: Documentation records the design, implementation, and testing details, making the project easier to maintain and explain during interviews.

Q2. Why do we commit after completing a module instead of after every small change?

Answer: A module-level commit creates meaningful milestones in Git history, making it easier to review, revert, and understand project progress.