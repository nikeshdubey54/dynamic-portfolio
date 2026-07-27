# Module 06 - Projects Module

## Module Information

- Module Number: 06
- Module Name: Projects Module
- Status: In Progress

---

## Module Status

| Phase | Status |
|--------|--------|
| ✅ Phase 1 – Projects App Creation | Completed |
| ⏳ Phase 2 – URL Configuration | Pending |
| ⏳ Phase 3 – Project Model Design | Pending |
| ⏳ Phase 4 – Admin Panel Registration | Pending |
| ⏳ Phase 5 – Database Migration | Pending |
| ⏳ Phase 6 – Project View | Pending |
| ⏳ Phase 7 – Project Template | Pending |
| ⏳ Phase 8 – Dynamic Project Display | Pending |
| ⏳ Phase 9 – Project Detail Page | Pending |
| ⏳ Phase 10 – Featured Projects | Pending |
| ⏳ Phase 11 – Final Testing | Pending |
| ⏳ Phase 12 – Documentation & Git | Pending |

---

# Phase 1 – Projects App Creation

## Objective

Create the Projects app and register it in the Django project.

### Files Created

- projects/

### Files Modified

- portfolio/settings.py

### Result

Projects app successfully created and registered.

Status:

✅ Completed

🎤 Interview Questions
Q1. Why do we create a separate app for Projects?

Answer:
To keep all project-related models, views, URLs, templates, and admin configuration in one modular application, making the project easier to maintain and extend.

Q2. Why register the app in INSTALLED_APPS?

Answer:
Without registering it, Django will not detect its models, migrations, templates, or admin configuration.

# Phase 2 – URL Configuration

## Objective

Configure URL routing for the Projects app.

### Files Created

- projects/urls.py

### Files Modified

- portfolio/urls.py

### Result

Projects URL configuration completed successfully.

Status:

✅ Completed

🎤 Interview Questions
Q1. Why do we create urls.py inside an app?

Answer:
To keep URL routing modular. Each app manages its own routes, making the project easier to maintain.

Q2. Why do we use include() in portfolio/urls.py?

Answer:
include() delegates URL handling to the respective app, keeping the main URL configuration clean and organized.

# Phase 3 – Project Model Design

## Objective

Create the Project model to store project information dynamically.

### Model Fields

- title
- short_description
- image
- technologies
- github_link
- live_demo
- featured
- created_at

### Special Methods

- __str__()

### Result

Project model created successfully.

Status:

✅ Completed

🎤 Interview Questions
Q1. Why do we use ImageField instead of CharField for images?

Answer:
ImageField is designed to handle image uploads and integrates with Django's media file system.

Q2. Why are github_link and live_demo marked with blank=True?

Answer:
Some projects may not have a GitHub repository or live demo. blank=True makes these fields optional in forms.

Q3. What is the purpose of the featured field?

Answer:
It allows selected projects to be highlighted separately on the portfolio.

Q4. Why do we use auto_now_add=True?

Answer:
It automatically stores the date and time when a project is created and doesn't change on future updates.

# Phase 4 – Admin Panel Registration

## Objective

Register the Project model in Django Admin.

### Files Modified

- projects/admin.py

### Admin Features

- list_display
- list_filter
- search_fields

### Result

Project model registered successfully in Django Admin.

Status:

✅ Completed
🎤 Interview Questions
Q1. Why do we register models in admin.py?

Answer:
To manage database records through Django's built-in Admin Panel without writing custom CRUD pages.

Q2. What is list_display?

Answer:
list_display specifies which model fields are shown as columns in the Django Admin list view.

Q3. What is the purpose of list_filter?

Answer:
It adds filter options in the Admin Panel, making it easier to view records based on specific field values.

Q4. What does search_fields do?

Answer:
It enables the search box in the Admin Panel, allowing records to be searched using the specified fields.

# Phase 4 – Database Migration

## Objective

Create the Project table in MySQL database.

### Commands Used

python manage.py makemigrations

python manage.py migrate

### Result

- Project table created successfully.
- Project model available in Django Admin.

Status:

✅ Completed

# Phase 5 – Project View

## Objective

Create a view to fetch all projects from the database and send them to the template.

### Files Modified

- projects/views.py

### Functions

- projects()

### Database Query

Project.objects.all().order_by('-created_at')

### Result

Project view created successfully.

Status:

✅ Completed

🎤 Interview Questions
Q1. Why do we import Project in views.py?

Answer:

To retrieve project data from the database and display it on the web page.

Q2. What does Project.objects.all() do?

Answer:

It fetches all records from the Project table.

Q3. Why do we use .order_by('-created_at')?

Answer:

It sorts the projects in descending order based on creation date, so the newest projects appear first.

# Phase 6 – URL Configuration

## Objective

Configure URL routing for the Projects module.

### Files Created

- projects/urls.py

### Files Modified

- portfolio/urls.py

### URL Added

/projects/

### Result

Projects module successfully connected with the main project.

Status:

✅ Completed

🎤 Interview Questions
Q1. Why do we create a separate urls.py inside each app?

Answer:

To keep routing modular and organized. Each app manages its own URLs independently.

Q2. What is the purpose of include()?

Answer:

include() passes URL handling to another URL configuration, making the main urls.py cleaner and easier to maintain.

Q3. Why didn't we configure URLs before creating the view?

Answer:

Because the URL references views.projects. If the view doesn't exist yet, Django raises an AttributeError.

# Phase 7 – Projects Template

## Objective

Create the Projects page template.

### Files Created

- projects/templates/projects/projects.html

### Features

- Bootstrap Cards
- Dynamic Project Loop
- Project Image
- Project Title
- Short Description
- Empty State Message

### Result

Projects template created successfully.

Status:

✅ Completed

🎤 Interview Questions
Q1. Why do we use {% for %} in Django templates?

Answer:

To iterate through data passed from the view and display multiple records dynamically.

Q2. What is the purpose of {% empty %}?

Answer:

It displays an alternative message when the queryset is empty.

Q3. What does truncatewords:20 do?

Answer:

It limits the displayed text to the first 20 words, making cards cleaner and preventing overly long descriptions.

# Phase 8 – Dynamic Project Display

## Objective

Display project details dynamically on the Projects page.

### Features Added

- Project Image
- Project Title
- Short Description
- Technologies
- Featured Badge
- GitHub Button
- Live Demo Button

### Result

Dynamic project cards displayed successfully.

Status:

✅ Completed

🎤 Interview Questions
Q1. Why do we use {% if project.github_link %}?

Answer:
To display the GitHub button only when a GitHub link is available.

Q2. Why do we use target="_blank"?

Answer:
It opens the GitHub or Live Demo link in a new browser tab without leaving the portfolio website.

Q3. What is the benefit of the featured badge?

Answer:
It highlights important projects, making them more noticeable to recruiters and visitors.

# Phase 9 – Project Detail Page

## Objective

Create a dedicated detail page for each project.

### Files Modified

- projects/views.py
- projects/urls.py
- projects/templates/projects/projects.html

### Files Created

- projects/templates/projects/project_detail.html

### Features

- Dynamic Project Detail Page
- URL Parameter
- get_object_or_404()
- GitHub Button
- Live Demo Button

### Result

Project Detail Page created successfully.

Status:

✅ Completed
🎤 Interview Questions
Q1. Why do we use get_object_or_404()?

Answer:

It fetches the requested object. If the object doesn't exist, Django automatically returns a 404 Not Found page instead of crashing.

Q2. Why do we use <int:id> in the URL?

Answer:

It captures the project's ID from the URL and passes it to the view so the correct project can be displayed.

Q3. Why create a separate detail page?

Answer:

It keeps the projects list clean while allowing users to view complete information about a selected project.

# Phase 10 – Featured Projects

## Objective

Display featured projects separately from all projects.

### Files Modified

- projects/views.py
- projects/templates/projects/projects.html

### Features

- Featured Projects Query
- Separate Featured Section
- Dynamic Rendering

### Result

Featured projects displayed successfully.

Status:

✅ Completed

🎤 Interview Questions
Q1. Why do we use filter(featured=True)?

Answer:
It retrieves only those projects whose featured field is set to True.

Q2. What is the difference between all() and filter()?

Answer:

all() returns every record.
filter() returns only records matching the given condition.
Q3. Why keep Featured Projects separate?

Answer:
It highlights the best or most important projects, making them more visible to recruiters and visitors.

# Module 06 – Projects

## Objective

Develop a dynamic Projects module for the portfolio website.

## Features

- Project Model
- Admin Management
- Dynamic Projects List
- Project Detail Page
- Featured Projects
- GitHub Link
- Live Demo Link
- Image Upload
- Bootstrap Cards
- Dynamic Rendering

## Testing

- Projects Page
- Detail Page
- Featured Projects
- Admin CRUD
- Empty State

## Result

Projects Module completed successfully.

Status:

✅ Module Completed