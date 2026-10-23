# HireReady AI — Full-Stack AI Interview Preparation Platform

HireReady AI is a modern, full-stack AI interview preparation platform designed to help job seekers practice **HR Interviews**, **Technical Interviews**, and **Combined Interviews (HR + Technical)** for any role with personalized, intelligent feedback.

---

## 🚀 Key Features

1. **Three Interview Modes**:
   - **HR Interview**: Behavioral and situational questions using the STAR framework (Situation, Task, Action, Result).
   - **Technical Interview**: Deep technical questions, architecture discussions, debugging, code analysis, and edge cases.
   - **Combined Interview**: Balanced hybrid interview with ~30% HR and ~70% technical questions.

2. **Dedicated Software Engineer Question Bank (125+ Questions)**:
   - Covers 5 core technologies: **Python (25)**, **HTML (25)**, **CSS (25)**, **JavaScript (25)**, and **SQL (25)**.
   - Filter by single technology, all 5, or a custom combination.

3. **400+ Verified Technical Question Bank**:
   - Permanent database-backed question bank across 12 predefined technical roles:
     - Software Engineer (125 Qs across Python, HTML, CSS, JS, SQL)
     - Python Developer (25 Qs)
     - Frontend Developer (25 Qs)
     - Backend Developer (25 Qs)
     - Full-Stack Developer (25 Qs)
     - Java Developer (25 Qs)
     - React Developer (25 Qs)
     - SQL Developer (25 Qs)
     - Data Analyst (25 Qs)
     - QA / Software Tester (25 Qs)
     - DevOps Engineer (25 Qs)
     - Cybersecurity Analyst (25 Qs)
   - Pre-seeded via Django management command.

4. **Custom Role Support**:
   - Enter any job role (e.g. *Bioinformatics Scientist*, *Embedded Systems Engineer*). The AI dynamically generates role-specific interview questions.

5. **Voice & Text Interaction**:
   - Integrated Speech Synthesis (AI voice reads questions aloud).
   - Real-time Speech-to-Text dictation with live preview and edit buffer before submission.
   - Syntax-highlighted code block viewer with copy-to-clipboard for technical problems.
   - Monospace code mode toggle for typing code/SQL responses.

6. **Separate HR & Technical Evaluation Rubrics**:
   - **Technical Rubric**: Accuracy (35%), Depth & Completeness (30%), Problem Solving & Edge Cases (25%), Clarity (10%).
   - **HR Rubric**: Relevance (30%), Clarity & Structure (25%), Examples & STAR Method (25%), Professional Communication (20%).
   - Displays correct points, missing points, and sample improved answers.

7. **Comprehensive Performance Reports**:
   - Side-by-side Overall Practice Score, HR Score, and Technical Score.
   - Separate HR strengths/improvements and Technical strengths/improvements.
   - Print-friendly layout (`@media print`).

8. **Security & Authentication**:
   - JWT authentication (Django REST Framework SimpleJWT).
   - Strict per-user data isolation.
   - Backend prompt injection protection and question validation.

---

## 🛠️ Technology Stack

- **Frontend**: React 18, Vite, React Router v6, Lucide Icons, Web Speech API, Canvas Confetti.
- **Styling**: Vanilla CSS design system with custom glassmorphic navy & purple theme.
- **Backend**: Python 3.10+, Django 5, Django REST Framework, SimpleJWT, Python-dotenv, Django CORS Headers.
- **AI Integration**: Google Gemini API via official Google GenAI Python SDK (`gemini-3.5-flash-lite`), with fallback deterministic mock engine for offline testing.

---

## 🏁 Quick Start Guide

### 1. Prerequisites
- Python 3.10+
- Node.js 18+ & npm
- Git

### 2. Backend Setup

```bash
cd backend

# Create and activate virtual environment
python -m venv venv
.\venv\Scripts\activate   # Windows (or source venv/bin/activate on macOS/Linux)

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
# Copy .env.example to .env:
cp .env.example .env

# Run database migrations
python manage.py migrate

# Seed the 400 verified technical questions
python manage.py seed_questions

# Run automated tests
python manage.py test

# Start Django development server (Port 8000)
python manage.py runserver 127.0.0.1:8000
```

### 3. Frontend Setup

```bash
cd frontend

# Install npm dependencies
npm install

# Start Vite dev server (Port 5173)
npm run dev
```

The app will be available at:
- **Frontend**: [http://localhost:5173/](http://localhost:5173/)
- **Backend API**: [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/)

---

## ⚙️ Environment Variables

### Backend (`backend/.env`)
| Variable | Description | Default |
|---|---|---|
| `SECRET_KEY` | Django secret key | (Set your own secret key in production) |
| `DEBUG` | Enable debug mode | `True` |
| `ALLOWED_HOSTS` | Allowed hostnames | `localhost,127.0.0.1` |
| `GEMINI_API_KEY` | Google Gemini API key | (Optional; fallback mock engine used if empty) |
| `GEMINI_MODEL` | Gemini model name | `gemini-3.5-flash-lite` |
| `CORS_ALLOWED_ORIGINS` | Permitted frontend origins | `http://localhost:5173,http://127.0.0.1:5173` |

### Frontend (`frontend/.env`)
| Variable | Description | Default |
|---|---|---|
| `VITE_API_URL` | Base backend API endpoint | `http://127.0.0.1:8000/api` |

---

## 🧪 Testing

Run backend tests:
```bash
cd backend
python manage.py test interviews
```
All 11 unit tests verify question bank counts, interview creation, technology filtering, ~30/70 combined distribution, evaluation rubrics, report generation, and security isolation.
