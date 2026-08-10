### Module 08 – Contact Module
7-Phase Plan
Phase 01 – App Setup + Model + Admin
Phase 02 – URL + View + Contact Form
Phase 03 – Contact Template + Dynamic Form
Phase 04 – Form Validation + Message Handling
Phase 05 – Professional UI + Animation
Phase 06 – Responsive + Error Handling + Optimization
Phase 07 – Final Testing + Documentation + Git

# Module 08 — Contact Module

## Overview

Module 08 me portfolio ke liye complete Contact Module develop kiya gaya.

### Main Features

* Contact page
* Contact form
* Form validation
* Database message storage
* Django Admin integration
* Bootstrap Toast
* Navbar Contact link
* Professional UI
* Responsive design
* Final testing

---

## Phase 1 — Contact App Setup

* Contact Django app create kiya.
* App ko `INSTALLED_APPS` me add kiya.
* Contact app ke templates aur basic structure setup kiye.
* Contact page ka URL configure kiya.

---

## Phase 2 — Contact Model

* Contact messages store karne ke liye model create kiya.
* Main fields:

  * Name
  * Email
  * Subject
  * Message
  * Created At
  * Is Read
* `is_read` field ka default `False` rakha.
* Migrations create aur apply kiye.

### Commands

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## Phase 3 — Contact Admin & Form

* Contact model ko Django Admin me register kiya.
* Admin panel me contact messages view aur manage kiye.
* Contact form create kiya.
* Name, Email, Subject aur Message fields add kiye.
* CSRF protection add ki.
* Required field validation implement ki.
* Email validation implement ki.
* Submitted messages database me save kiye.

---

## Phase 4 — Contact UI & Navbar

* Navbar me Contact link add kiya.
* `Let's Connect` section create kiya.
* Email, Location aur Availability information add ki.
* `Send Me a Message` form section create kiya.
* Professional cards aur shadows add kiye.
* Contact icons par hover effect add kiya.
* Existing portfolio ke blue/white color combination ko maintain kiya.

---

## Phase 5 — Bootstrap Toast

* Successful form submission ke liye Bootstrap Toast implement kiya.
* Success message user ko display kiya.
* Toast ko 4 seconds ke baad automatically hide kiya.
* Toast close button add kiya.
* Bootstrap JS ko `base.html` me globally load kiya.

---

## Phase 6 — Responsive Design

* Contact page ko desktop, tablet aur mobile ke liye responsive banaya.
* Mobile par contact cards ko vertically stack kiya.
* Form fields ko mobile screen ke according adjust kiya.
* Submit button ko mobile par full width kiya.
* Horizontal overflow issue fix kiya.
* Contact container structure ko correct kiya.
* `.contact-section` class properly add ki.

### Tested Screen Sizes

* 320 × 640
* 375 × 667
* 390 × 844

---

## Phase 7 — Final Testing & Cleanup

* Empty form validation test ki.
* Required field validation test ki.
* Invalid email validation test ki.
* Successful form submission test ki.
* Bootstrap Toast test ki.
* Toast auto-hide test ki.
* Django Admin me message save hona verify kiya.
* Responsive layout verify kiya.
* Django system check run kiya.

### Command

```bash
python manage.py check
```

---

# Interview / Viva Questions

## 1. Django Form kya hai?

Django Form user se data lene, validate karne aur process karne ke liye use hota hai.

## 2. CSRF Token kya hai?

CSRF token Django form ko Cross-Site Request Forgery attacks se protect karta hai.

## 3. EmailField ka use kya hai?

`EmailField` email address ko validate karne ke liye use hota hai.

## 4. BooleanField kya hota hai?

`BooleanField` `True` ya `False` value store karta hai.

## 5. `is_read` field ka use kya hai?

`is_read` field se pata chalta hai ki admin ne contact message read kiya hai ya nahi.

## 6. `auto_now_add=True` kya karta hai?

Object create hone ke time automatically current date aur time save karta hai.

## 7. `makemigrations` aur `migrate` me kya difference hai?

`makemigrations` model changes ke liye migration files create karta hai, jabki `migrate` un changes ko database me apply karta hai.

## 8. Django Admin ka use kya hai?

Django Admin database data ko easily view aur manage karne ke liye built-in interface provide karta hai.

## 9. Bootstrap Toast kya hai?

Bootstrap Toast ek temporary notification component hai jo user ko success ya other messages show karta hai.

## 10. Toast ko automatically hide kaise kiya?

JavaScript me `delay: 4000` set karke Toast ko 4 seconds ke baad automatically hide kiya.

## 11. GET aur POST me kya difference hai?

GET generally data retrieve karne ke liye aur POST data submit ya create karne ke liye use hota hai.

## 12. `request.POST` kya karta hai?

`request.POST` POST request ke through submit kiya gaya form data access karta hai.

## 13. Django Messages Framework kya hai?

Django Messages Framework user ko temporary success, error, warning ya information messages show karne ke liye use hota hai.

## 14. Responsive Design kya hai?

Responsive design website ko different screen sizes jaise desktop, tablet aur mobile par properly display karne ki technique hai.

## 15. `col-md-6` ka kya meaning hai?

Bootstrap me `col-md-6` medium aur larger screens par 12-column grid me se 6 columns ki width leta hai.

## 16. `python manage.py check` ka use kya hai?

Ye Django project ki configuration aur common errors ko check karne ke liye use hota hai.

---

## Module 08 Status

**Module 08 — Contact Module: Completed ✅**
