# Module 03 - Home App & Base Project Structure

## Module Information

- **Module Number:** 03
- **Module Name:** Home App & Base Project Structure
- **Status:** In Progress

---

# Module Objective

Create the first Django application (`home`) and build the foundation of the Dynamic Portfolio CMS.

---

# Module 03 Status

| Phase | Status |
|--------|---------|
| ✅ Phase 1 – Home App Creation | Completed |
| ✅ Phase 2 – URL Configuration | Completed |
| ✅ Phase 3 – Templates Structure | Completed |
| ✅ Phase 4 – Base Template | Completed |
| ✅ Phase 5 – Navbar Development | Completed |
| ✅ Phase 6 – Footer Development | Completed |
| ✅ Phase 7 – Home Page Development | Completed |
| ✅ Phase 8 – Static Assets Integration | Completed |
| ✅ Phase 9 – Final Testing | Completed |
| ✅ Phase 10 – Documentation & Git | Completed |

---

# Expected Outcome

After completing this module, the project will have:

- Professional Home App
- URL Routing
- Base Template
- Responsive Navbar
- Responsive Footer
- Home Page Structure
- Static Assets Integration
- Clean Project Architecture

---

# Learning Outcome

After completing this module, I will understand:

- Django App Structure
- URL Routing
- Template Inheritance
- Base Template Concept
- Reusable Components
- Project Architecture

---

# Module Status

🔄 In Progress

---

# Phase 1 – Home App Creation

## Objective

Create the first Django application (`home`) and register it in the Django project.

## Files Created

- home/
- home/views.py
- home/models.py
- home/admin.py
- home/apps.py
- home/tests.py
- home/migrations/

## Files Modified

- portfolio/settings.py

## Changes Made

- Created the `home` application.
- Registered the application inside `INSTALLED_APPS`.
- Verified the project by running the development server.

## Result

The `home` application was successfully integrated into the Django project.

## Status

✅ Completed

## 🎤 Interview Questions

Q1. Django Project aur App me kya difference hai?

Answer:

Project → Complete website/application.
App → Website ka ek feature/module.
Q2. INSTALLED_APPS ka purpose kya hai?

Answer:

INSTALLED_APPS Django ko batata hai ki project me kaun-kaun se applications active hain. Agar app yahan register nahi hoga, to Django uske models, templates aur admin configuration ko load nahi karega.

Q3. startapp command kya karti hai?

Answer:

Ye command ek naya Django app create karti hai jisme required default files aur folders automatically ban jate hain.


---

# Phase 2 – URL Configuration

## Objective

Configure URL routing for the `home` application and connect it with the main project.

## Files Created

- home/urls.py

## Files Modified

- home/views.py
- portfolio/urls.py

## Changes Made

- Created `home/urls.py`.
- Connected `home` app with the main project using `include()`.
- Created the first view function.
- Verified URL routing using the development server.

## Result

The root URL (`/`) is now handled by the `home` application.

## Status

✅ Completed

## 🎤 Interview Questions
Q1. include() ka use kyu karte hain?

Answer:

include() project ke URLs ko alag-alag apps me divide karta hai. Isse project modular aur maintainable banta hai.

Q2. View kya hoti hai?

Answer:

View ek Python function ya class hoti hai jo request receive karti hai, usko process karti hai aur response return karti hai.

Q3. URL Routing kya hoti hai?

Answer:

URL Routing browser se aayi request ko sahi view function tak pahunchane ka process hai.

---

# Phase 3 – Templates Structure

## Objective

Create a professional template structure and render the first HTML page using Django.

## Files Created

- templates/base.html
- templates/home/index.html

## Files Modified

- home/views.py

## Changes Made

- Created the global templates directory.
- Created the first HTML page (`index.html`).
- Replaced `HttpResponse` with `render()`.
- Verified HTML rendering using Django templates.

## Result

The Home page is now rendered using Django's template engine instead of a plain HTTP response.

## Status

✅ Completed

## 🎤 Interview Questions
Q1. render() aur HttpResponse() me kya difference hai?

Answer:

HttpResponse() directly text ya HTML return karta hai.
render() HTML template ko process karke response return karta hai aur usme dynamic data bhi bhej sakte hain.
Q2. Django me Templates ka purpose kya hai?

Answer:

Templates presentation layer hoti hain. Inke through HTML pages generate kiye jaate hain aur dynamic data display kiya jata hai.

Q3. Global templates folder kyu banaya?

Answer:

Global templates folder se project ki template files centrally manage hoti hain aur reusable layout banana aasaan ho jata hai.


---

# Phase 4 – Base Template

## Objective

Create a reusable base template using Django Template Inheritance.

## Files Created

- templates/base.html
- static/css/style.css
- static/js/main.js

## Files Modified

- templates/home/index.html

## Changes Made

- Created the global `base.html` template.
- Integrated Bootstrap 5 via CDN.
- Added custom CSS and JavaScript files.
- Implemented Django Template Inheritance using `{% extends %}` and `{% block %}`.
- Updated the Home page to inherit from `base.html`.

## Result

The project now uses a reusable base layout, making future pages easier to build and maintain.

## Status

✅ Completed

## 🎤 Interview Questions
Q1. What is Template Inheritance?

Answer:

Template Inheritance allows multiple HTML pages to reuse a common layout (base.html) while defining only their unique content.

Q2. What is the purpose of {% extends %}?

Answer:

{% extends %} tells Django that the current template inherits from another template, usually base.html.

Q3. What is the purpose of {% block %}?

Answer:

{% block %} defines replaceable sections in a parent template. Child templates can override these sections with their own content.

Q4. Why do we create a base.html file?

Answer:

To avoid repeating common HTML such as the <head>, Bootstrap links, footer, and scripts on every page. It improves maintainability and keeps the project organized.

---

# Phase 5 – Professional Navbar Development

## Objective

Create a reusable and responsive navigation bar for the entire project.

## Files Created

- templates/includes/navbar.html

## Files Modified

- templates/base.html

## Changes Made

- Created a reusable navigation bar.
- Integrated Bootstrap responsive navbar.
- Included the navbar in the global `base.html`.
- Added navigation links for future pages.

## Result

The navigation bar is now displayed across all pages through template inclusion.

## Status

✅ Completed

## 🎤 Interview Questions
Q1. Why do we use {% include %} in Django?

Answer:

{% include %} is used to reuse common template components like the navbar, footer, sidebar, and forms. It reduces duplicate code and makes maintenance easier.

Q2. What is the advantage of a reusable Navbar?

Answer:

A reusable navbar is written once and used across all pages. Any future changes only need to be made in one file.

Q3. What does navbar-expand-lg mean in Bootstrap?

Answer:

It keeps the navbar expanded on large screens and automatically collapses it into a mobile menu on smaller screens.

---

# Phase 6 – Professional Footer Development

## Objective

Create a reusable and responsive footer for the entire website.

## Files Created

- templates/includes/footer.html

## Files Modified

- templates/base.html

## Changes Made

- Created a reusable footer component.
- Added Quick Links section.
- Added Contact Information section.
- Added Copyright section.
- Included the footer in the global `base.html`.

## Result

The footer is now displayed across all pages through template inclusion.

## Status

✅ Completed

##  🎤 Interview Questions
Q1. Why should a footer be reusable?

Answer:

A reusable footer avoids duplicate code, keeps the project organized, and allows changes to be made in one place that automatically appear on every page.

Q2. Why is the footer included in base.html?

Answer:

Because base.html is inherited by all pages. Including the footer there ensures it appears consistently throughout the website.

Q3. What common information is usually displayed in a website footer?

Answer:

A footer typically contains:

Copyright information
Quick navigation links
Contact details
Social media links
Company or personal information


---

# Phase 7 – Home Page Development (Part 1)

## Objective

Develop the Hero Section of the Home page.

## Files Modified

- templates/home/index.html
- static/css/style.css

## Changes Made

- Created the Hero Section.
- Added developer introduction.
- Added professional heading.
- Added Resume button.
- Added Contact button.
- Added placeholder profile image.
- Improved layout using Bootstrap Grid.

## Result

The Home page now displays a professional Hero Section with responsive layout.

## Status

✅ Part 1 Completed

## 🎤 Interview Questions
Q1. Why is the Hero Section important?

Answer:
The Hero Section is the first section users see when they visit a website. It creates the first impression and introduces the person or business.

Q2. Why do we use the Bootstrap Grid System?

Answer:
The Bootstrap Grid System helps create responsive layouts that automatically adapt to different screen sizes.

Q3. Why use a placeholder image during development?

Answer:
A placeholder image allows developers to complete and test the page layout before the final image is available.

---

# Phase 7 – Home Page Development (Part 2)

## Objective

Enhance the Hero Section by adding a professional profile card, statistics and social buttons.

## Files Modified

- templates/home/index.html
- static/css/style.css

## Changes Made

- Added Profile Card.
- Added Circular Profile Image.
- Added Developer Information.
- Added Project Statistics.
- Added Social Buttons.
- Improved Card Styling.

## Result

The Hero Section now contains a professional profile card with statistics and action buttons.

## Status

✅ Part 2 Completed

## 🎤 Interview Questions
Q1. Why do we use Bootstrap Cards?

Answer:
Bootstrap Cards provide a clean and reusable layout for displaying grouped information such as profile details, projects or services.

Q2. Why is a statistics section useful in a portfolio?

Answer:
It quickly highlights achievements like completed projects, technical skills and experience, helping visitors understand the developer's profile at a glance.

Q3. Why should social links be visible on the Home page?

Answer:
Visible social links make it easier for recruiters, clients and visitors to connect and verify professional profiles.

---

# Phase 7 – Home Page Development (Part 3)

## Objective

Refactor the Home page into reusable templates and add the About Preview section.

## Files Created

- templates/home/hero.html
- templates/home/about_preview.html
- templates/home/skills_preview.html
- templates/home/projects_preview.html
- templates/home/services_preview.html
- templates/home/contact_cta.html
- templates/home/testimonials.html

## Files Modified

- templates/home/index.html
- static/css/style.css

## Changes Made

- Moved the Hero Section into a separate template.
- Created the About Preview template.
- Updated `index.html` to include reusable templates.
- Added smooth hover effects.
- Improved page spacing.
- Followed modular template architecture.

## Result

The Home page is now modular, easier to maintain, and follows a professional Django project structure.

## Status

✅ Part 3 Completed

## 🎤 Interview Questions
Q1. Why did you move the Hero Section into a separate file?

Answer:
To make the code modular, reusable, and easier to maintain. Each section can be updated independently without affecting the rest of the page.

Q2. Why is index.html kept so small?

Answer:
index.html acts as the main page controller. It assembles different reusable sections using {% include %}, keeping the project organized.

Q3. What is the benefit of a modular template architecture?

Answer:
It improves readability, simplifies debugging, encourages code reuse, and is easier for teams to work on.

---

# Phase 7 – Home Page Development (Part 4)

## Objective

Complete the Home page by adding Skills Preview, Projects Preview and Contact CTA sections.

## Files Modified

- templates/home/index.html
- templates/home/skills_preview.html
- templates/home/projects_preview.html
- templates/home/contact_cta.html
- static/css/style.css

## Changes Made

- Added Skills Preview section.
- Added Featured Projects section.
- Added Contact CTA section.
- Updated Home page template includes.
- Improved card hover effects.

## Result

The Home page now contains all major landing page sections and follows a modular template architecture.

## Status

✅ Part 4 Completed

## Tuesday 9:14 AM
ok mai screenshot bhwj rha hu dekho ki akaha tk kaam hua h 
pr bhai tumne ek includes folder banaya tha jis me footer.html h , navbar.html, h or ek folder h home k naam se jis me index.html h or index .html me sirf hero section hi h or avhi bol rhe ki Footer se pehle, Hero Section ke niche ye code add karo: index.html me ye code add kro itna confusing kahe kr rhe ho

Bhai, tum bilkul sahi ho. Aur ye meri galti thi. 👍

Main project ko aur better banane ki koshish me beech-beech me architecture improve kar raha tha, lekin usse tum confuse ho gaye. Ye nahi hona chahiye tha.

Ab ek rule fix karte hain:

❌ Ab main beech me architecture change nahi karunga.
❌ "Baad me karenge" bolkar current phase ko adhura nahi chhodunga.
✅ Jo phase start hoga, usko usi time complete karenge.
✅ Agar future improvement hoga, to uska naam "Future Enhancement" hoga, current phase ka part nahi.
Ab se hamara workflow final hai

Har phase me main ye order follow karunga:

🎯 Objective
📚 Theory
📝 Step by Step Code
📄 Documentation
🎤 Interview Questions
🧪 Testing Checklist
✅ Phase Complete

Uske baad hi next phase.

Aur ek aur promise

Ab se main sirf code nahi dunga.

Main ye sochkar dunga ki:

"Ye project GitHub par dekhkar recruiter bole - is bande ko Django architecture aata hai."

Isliye kabhi-kabhi improvement suggest karunga, lekin current phase complete karne ke baad, beech me nahi.

Abhi hum kya karenge?

Tumne Phase 7 Part 2 tak Hero bana liya hai.

Main suggest karta hoon:

Hero ko hero.html me shift karte hain.
index.html ko clean karte hain.
about_preview.html banate hain.

Bas itna hi. Koi aur extra feature nahi.

Jab ye complete ho jayega tab hum Skills Preview par jayenge.

Aur ek last baat: ab se main is project ko tutorial ki tarah nahi, mentor ki tarah lead karunga. Har decision ek baar final hoga, aur bina wajah usko change nahi karenge. Isse documentation bhi clean rahegi aur tumhe confusion bhi nahi hoga. 💪

part 3 phir se do 

Bilkul bhai. 💯 Is baar Part 3 final version de raha hoon. Iske baad architecture change nahi hoga. Hum isi structure ko project ke end tak follow karenge.

📘 Module 03 – Phase 7 (Part 3)
Home Page Modular Structure & About Preview
🎯 Objective

Is phase ka goal hai:

Hero Section ko alag file me move karna.
Home Page ko modular banana.
About Preview section add karna.
Clean aur industry-standard template architecture banana.
📂 Step 1 – Home Folder Structure

templates/home/ ke andar ye files banao:

templates/
│
├── home/
│   ├── index.html
│   ├── hero.html
│   ├── about_preview.html
│   ├── skills_preview.html
│   ├── projects_preview.html
│   ├── services_preview.html
│   ├── contact_cta.html
│   └── testimonials.html

⚠️ Abhi sirf hero.html aur about_preview.html me code likhenge. Baaki files abhi empty reh sakti hain.

📂 Step 2 – Hero Section Shift

Abhi templates/home/index.html me jo Hero Section hai:

<section class="py-5">
....
</section>

Us poore section ko Cut karo.

Aur

templates/home/hero.html

me Paste kar do.

⚠️ Hero ke andar koi change mat karna.

Resume Button wahi rahega.
Contact Button wahi rahega.
Scroll Button abhi nahi add karna.
📂 Step 3 – index.html

Ab templates/home/index.html me sirf ye code hona chahiye:

{% extends 'base.html' %}

{% block title %}
Home | Dynamic Portfolio
{% endblock %}

{% block content %}

{% include 'home/hero.html' %}

{% include 'home/about_preview.html' %}

{% endblock %}

Ye file ab sirf Home Page ka controller ban gayi hai.

📂 Step 4 – About Preview

Create

templates/home/about_preview.html

Paste:

<section id="about-section" class="py-5 bg-white">

    <div class="container">

        <div class="row align-items-center">

            <div class="col-lg-6">

                <img
                    src="https://placehold.co/500x350"
                    class="img-fluid rounded shadow"
                    alt="About Me">

            </div>

            <div class="col-lg-6">

                <h2 class="fw-bold mb-4">

                    About Me

                </h2>

                <p class="lead">

                    I am a passionate Python Full Stack Developer who enjoys building modern and scalable web applications using Django, Python, MySQL, HTML, CSS, JavaScript and Bootstrap.

                </p>

                <p>

                    I continuously improve my skills, learn new technologies and build professional projects that solve real-world problems.

                </p>

                <a href="#"
                   class="btn btn-primary">

                    Read More

                </a>

            </div>

        </div>

    </div>

</section>
📂 Step 5 – CSS

Open

static/css/style.css

Niche add karo:

section{
    padding:80px 0;
}

.card{
    transition:.3s;
}

.card:hover{
    transform:translateY(-8px);
}

.btn{
    transition:.3s;
}

.btn:hover{
    transform:translateY(-3px);
}
📂 Step 6 – Run Project
python manage.py runserver

Open:

http://127.0.0.1:8000/
✅ Expected Result
Navbar
        │
Hero Section
        │
About Preview
        │
Footer

Ab Home Page do alag sections me divide ho chuka hoga.

📄 Documentation

docs/Module-03.md

---

# Phase 7 – Home Page Development (Part 3)

## Objective

Refactor the Home page into reusable templates and add the About Preview section.

## Files Created

- templates/home/hero.html
- templates/home/about_preview.html
- templates/home/skills_preview.html
- templates/home/projects_preview.html
- templates/home/services_preview.html
- templates/home/contact_cta.html
- templates/home/testimonials.html

## Files Modified

- templates/home/index.html
- static/css/style.css

## Changes Made

- Moved the Hero Section into a separate template.
- Created the About Preview template.
- Updated `index.html` to include reusable templates.
- Added smooth hover effects.
- Improved page spacing.
- Followed modular template architecture.

## Result

The Home page is now modular, easier to maintain, and follows a professional Django project structure.

## Status

✅ Part 3 Completed
🎤 Interview Questions
Q1. Why did you move the Hero Section into a separate file?

Answer:
To make the code modular, reusable, and easier to maintain. Each section can be updated independently without affecting the rest of the page.

Q2. Why is index.html kept so small?

Answer:
index.html acts as the main page controller. It assembles different reusable sections using {% include %}, keeping the project organized.

Q3. What is the benefit of a modular template architecture?

Answer:
It improves readability, simplifies debugging, encourages code reuse, and is easier for teams to work on.

📌 Final Rule (Ab Kabhi Change Nahi Hoga)

Hum poore project me isi pattern ko follow karenge:

base.html
        │
        ├── navbar.html
        │
        ├── index.html
        │       ├── hero.html
        │       ├── about_preview.html
        │       ├── skills_preview.html
        │       ├── projects_preview.html
        │       ├── services_preview.html
        │       ├── contact_cta.html
        │       └── testimonials.html
        │
        └── footer.html

Is architecture ko ab hum project ke end tak maintain karenge. Har naye page (About, Projects, Contact, Blog) ke liye bhi isi tarah modular templates banayenge. Ye production-level Django projects me commonly use hone wala approach hai.

hone page dovelopment part 4 do ab

Perfect bhai. 🔥

Ab hum Module 03 – Phase 7 (Part 4) karenge.

⚠️ Ye Module 03 ka last development part hai. Iske baad Home Page ka base structure complete ho jayega.

📘 Module 03 – Phase 7 (Part 4)
Skills Preview + Projects Preview + CTA Section
🎯 Objective

Home Page ko complete feel dena by adding:

Skills Preview
Projects Preview
Contact Call-to-Action
📂 Step 1 – Skills Preview

Open:

templates/home/skills_preview.html

Paste this:

<section class="py-5 bg-light">

    <div class="container">

        <div class="text-center mb-5">

            <h2 class="fw-bold">My Skills</h2>

            <p class="text-muted">

                Technologies I use to build modern applications.

            </p>

        </div>

        <div class="row g-4">

            <div class="col-md-3">
                <div class="card shadow-sm text-center p-4">
                    <h4>Python</h4>
                </div>
            </div>

            <div class="col-md-3">
                <div class="card shadow-sm text-center p-4">
                    <h4>Django</h4>
                </div>
            </div>

            <div class="col-md-3">
                <div class="card shadow-sm text-center p-4">
                    <h4>MySQL</h4>
                </div>
            </div>

            <div class="col-md-3">
                <div class="card shadow-sm text-center p-4">
                    <h4>React</h4>
                </div>
            </div>

        </div>

    </div>

</section>
📂 Step 2 – Projects Preview

Open

templates/home/projects_preview.html

Paste

<section class="py-5">

    <div class="container">

        <div class="text-center mb-5">

            <h2 class="fw-bold">

                Featured Projects

            </h2>

        </div>

        <div class="row g-4">

            <div class="col-lg-4">

                <div class="card shadow">

                    <img src="https://placehold.co/600x400"
                         class="card-img-top">

                    <div class="card-body">

                        <h5>Dynamic Portfolio CMS</h5>

                        <p>

                            Professional portfolio developed using Django.

                        </p>

                    </div>

                </div>

            </div>

            <div class="col-lg-4">

                <div class="card shadow">

                    <img src="https://placehold.co/600x400"
                         class="card-img-top">

                    <div class="card-body">

                        <h5>E-Commerce Website</h5>

                        <p>

                            Online shopping application using Django.

                        </p>

                    </div>

                </div>

            </div>

            <div class="col-lg-4">

                <div class="card shadow">

                    <img src="https://placehold.co/600x400"
                         class="card-img-top">

                    <div class="card-body">

                        <h5>Blog Application</h5>

                        <p>

                            Blogging platform with Admin Panel.

                        </p>

                    </div>

                </div>

            </div>

        </div>

    </div>

</section>
📂 Step 3 – Contact CTA

Open

templates/home/contact_cta.html

Paste

<section class="bg-primary text-white py-5">

    <div class="container text-center">

        <h2>

            Let's Build Something Amazing Together

        </h2>

        <p class="mt-3">

            Looking for a Python Full Stack Developer?

        </p>

        <a href="#"
           class="btn btn-light btn-lg mt-3">

            Contact Me

        </a>

    </div>

</section>
📂 Step 4 – Update index.html

Replace with

{% extends 'base.html' %}

{% block title %}
Home | Dynamic Portfolio
{% endblock %}

{% block content %}

{% include 'home/hero.html' %}

{% include 'home/about_preview.html' %}

{% include 'home/skills_preview.html' %}

{% include 'home/projects_preview.html' %}

{% include 'home/contact_cta.html' %}

{% endblock %}
📂 Step 5 – CSS

style.css

Add

.card{

    transition:.3s;

}

.card:hover{

    transform:translateY(-10px);

}

.card img{

    height:220px;

    object-fit:cover;

}

section{

    scroll-margin-top:80px;

}
📄 Documentation

Add in Module-03.md

---

# Phase 7 – Home Page Development (Part 4)

## Objective

Complete the Home page by adding Skills Preview, Projects Preview and Contact CTA sections.

## Files Modified

- templates/home/index.html
- templates/home/skills_preview.html
- templates/home/projects_preview.html
- templates/home/contact_cta.html
- static/css/style.css

## Changes Made

- Added Skills Preview section.
- Added Featured Projects section.
- Added Contact CTA section.
- Updated Home page template includes.
- Improved card hover effects.

## Result

The Home page now contains all major landing page sections and follows a modular template architecture.

## Status

✅ Part 4 Completed
🎤 Interview Questions
Q1. Why is the Home page divided into multiple sections?

Answer:
A multi-section Home page introduces the developer, showcases skills and projects, and provides a clear call-to-action, helping visitors quickly understand the profile.

Q2. Why use reusable templates with {% include %}?

Answer:
Reusable templates improve maintainability, reduce duplicate code, and make it easier to update individual sections independently.

Q3. Why include a Call-to-Action (CTA) section?

Answer:
A CTA encourages visitors to take the next step, such as contacting the developer or exploring more projects, increasing engagement.

---

# Phase 8 – Static Assets Integration

## Objective

Organize all static resources into a professional folder structure.

## Files Created

- static/css/responsive.css
- static/css/animation.css
- static/js/main.js

## Folders Created

- static/images/
- static/images/profile/
- static/images/projects/
- static/images/services/
- static/images/skills/
- static/images/icons/
- static/images/hero/
- static/downloads/

## Files Modified

- templates/base.html

## Changes Made

- Added responsive stylesheet.
- Added animation stylesheet.
- Added JavaScript file.
- Created organized image directories.
- Created downloads folder for resume.
- Linked all static assets through `base.html`.

## Result

The project now has a scalable and production-ready static asset structure.

## Status

✅ Completed

## 🎤 Interview Questions
Q1. Why do we separate CSS into multiple files?

Answer:
Separating CSS into files like style.css, responsive.css, and animation.css improves organization, readability, and maintainability.

Q2. Why do we keep JavaScript in a separate file?

Answer:
Keeping JavaScript in external files makes the HTML cleaner, promotes code reuse, and simplifies debugging.

Q3. Why organize images into separate folders?

Answer:
It makes asset management easier, especially in large projects where profile images, project screenshots, icons, and service images serve different purposes.

---

# Phase 9 – Final Testing

## Objective

Verify all components of Module 03 before finalizing the module.

## Testing Performed

- Django Server Test
- Home Page Test
- Static Files Test
- Responsive Layout Test
- Template Structure Test
- Static Folder Test
- Database Migration Test
- Git Status Test

## Result

All components were tested successfully and the module is ready for version control.

## Status

✅ Completed

## 🎤 Interview Questions
Q1. Why do we test a module before committing it?

Answer:
Testing ensures that all features work correctly before saving them to version control. This helps prevent bugs from entering the project history.

Q2. Why run makemigrations even when no models were changed?

Answer:
It confirms that there are no pending model changes. If Django reports "No changes detected," the database schema is already synchronized.

Q3. Why test responsive behavior during development?

Answer:
A responsive layout ensures the application works correctly on desktops, tablets, and mobile devices, providing a consistent user experience.