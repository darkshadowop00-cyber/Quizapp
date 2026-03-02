# 🧠 QuizApp

A full-featured quiz web application built with **Django**. Users can register, take quizzes across multiple categories, earn badges for perfect scores, and track their performance on a personal dashboard.

---

## ✨ Features

- 🔐 **User Authentication** — Register, login, and logout
- 📚 **Multiple Categories** — Quizzes covering topics like Python, DBMS, OS, Java, HTML, CSS, JavaScript, Cloud Computing, and more
- 🎲 **Randomized Questions** — Every attempt serves a fresh, shuffled set of questions and answers
- 🏆 **Badge System** — Earn a badge for every category you ace with a perfect score
- 📊 **Dashboard** — View your attempt history and average score
- 👤 **Profile Page** — See all your earned badges and stats in one place
- 🔍 **Result Breakdown** — After each quiz, see a detailed answer-by-answer review

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Python / Django 5.x |
| Database | SQLite (default) |
| Frontend | HTML, CSS (custom templates) |
| Auth | Django built-in authentication |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- pip

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/darkshadowop00-cyber/Quizapp.git
cd Quizapp

# 2. Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply migrations
python manage.py migrate

# 5. Seed the database with quiz data
python manage.py shell < seed_data.py

# 6. (Optional) Seed badges
python manage.py shell < seed_badges.py

# 7. Create a superuser (for admin panel)
python manage.py createsuperuser

# 8. Run the development server
python manage.py runserver
```

Then open your browser at **http://127.0.0.1:8000**

---

## 📁 Project Structure

```
Quiz App/
├── quiz/                   # Main Django app
│   ├── models.py           # Category, Quiz, Question, Answer, Badge, UserProfile
│   ├── views.py            # All views (quiz list, take, result, dashboard, profile)
│   ├── urls.py             # App-level URL routing
│   ├── admin.py            # Django admin configuration
│   └── forms.py            # User registration form
├── quiz_project/           # Django project settings
│   ├── settings.py
│   └── urls.py
├── templates/              # HTML templates
│   ├── base.html
│   ├── quiz/
│   └── registration/
├── seed_data.py            # Main quiz seed script
├── seed_badges.py          # Badge seed script
├── manage.py
└── requirements.txt
```

---

## 🗂️ Quiz Categories

The app includes quizzes across a wide range of topics:

- Python, C, C++, Java
- HTML, CSS, JavaScript
- DBMS, Operating Systems, Computer Networks
- FLAT, Compiler Design, Software Design
- Cloud Computing, Data Structures, Algorithms
- ...and more!

---

## 🏅 Badge System

Earn a **category badge** by scoring **100%** on any quiz in that category. Badges are displayed on your profile page.

---

## 👤 Admin Panel

Access the Django admin at **http://127.0.0.1:8000/admin/** to manage:
- Categories & Quizzes
- Questions & Answers
- Badges
- User Profiles & Attempts

---

## 📸 Screenshots

> *(Add screenshots here once deployed)*

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👨‍💻 Author

**darkshadowop00-cyber** — [GitHub Profile](https://github.com/darkshadowop00-cyber)
