# 🚀 NoteFlow – Notes & Todo Management App

**NoteFlow** is a simple and efficient web application built using **Django** that allows users to manage their **notes and daily tasks** in one place.


## 📌 Features

### 🔐 Authentication

* User Registration
* Login & Logout
* Session-based authentication

### 📝 Notes Module

* Create sticky notes
* View all notes
* Edit notes
* Delete notes
* Notes are saved user-wise

### ✅ Todo Module

* Add tasks with status:

  * Active
  * Pending
  * Completed
* Edit tasks
* Delete tasks
* Color-coded UI based on task status

### 🎯 Dashboard

* Personalized welcome message
* Quick access to Notes and Todo

---

## 🛠️ Tech Stack

* **Backend:** Django (Python)
* **Frontend:** HTML, CSS, Bootstrap
* **Database:** SQLite (default Django DB)

---

## 📂 Project Structure

```
taskproject/
│
├── taskproject/       # Main project settings
├── taskapp/           # Main application
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│
├── db.sqlite3
└── manage.py
```

---

## ⚙️ Installation & Setup

1. Clone the repository:

```
git clone https://github.com/your-username/noteflow.git
cd noteflow
```

2. Create virtual environment:

```
python -m venv venv
venv\Scripts\activate   # Windows
```

3. Install dependencies:

```
pip install django
```

4. Run migrations:

```
python manage.py makemigrations
python manage.py migrate
```

5. Start server:

```
python manage.py runserver
```

6. Open browser:

```
http://127.0.0.1:8000/
```

---

## 🔐 Important Settings

Add in `settings.py`:

```python
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/page/'
LOGOUT_REDIRECT_URL = '/login/'
```

---

## 🚀 Future Improvements

* Edit/Delete using AJAX (no reload)
* Task filtering (Active / Completed)
* Drag & Drop tasks (Kanban style)
* User profile page
* Deployment (Render / Railway)

---

## 🙌 Author

**Naveenraj**
Aspiring Full Stack Developer 🚀

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
---
## Social Links
**Likedin:** https://www.linkedin.com/in/naveenraj-c-9b5b2729b/ 🚀

