# 🍽️ MealMatrix AI

> AI-powered meal recommendation system based on user mood.

---

## 📌 Overview

MealMatrix AI is a simple full-stack application that suggests meals based on how a user is feeling.
It connects a **Node.js backend** with a **FastAPI service** to generate real-time recommendations and display them through a modern web interface.

---

## ✨ Features

* Mood-based food recommendations
* Fast API communication between Node.js and FastAPI
* Simple and responsive frontend
* Real-time results display

---

## 🏗️ Tech Stack

| Layer      | Technology            |
| ---------- | --------------------- |
| Frontend   | HTML, CSS, JavaScript |
| Backend    | Node.js (Express)     |
| AI Service | FastAPI (Python)      |

---

## 🧠 How It Works

1. User selects or enters a mood
2. Frontend sends request to Node.js backend
3. Backend forwards request to FastAPI service
4. FastAPI returns food recommendations
5. Results are displayed on the UI

---

## 📂 Project Structure

```bash id="2m1lxt"
MealMatrix-AI/
│
├── api/                 # Node.js backend
│   ├── server.js
│   └── package.json
│
├── fastapi-backend/     # FastAPI service
│   ├── main.py
│   └── requirements.txt
│
├── public/              # Frontend
│   └── index.html
│
├── README.md
└── vercel.json
```

---

## ⚙️ Setup & Run

### 1. Clone the repository

```bash id="lp51y0"
git clone https://github.com/Anerig4/MealMatrix.git
cd MealMatrix
```

---

### 2. Start FastAPI server

```bash id="q06u0l"
cd fastapi-backend
pip install -r requirements.txt
uvicorn main:app --reload
```

---

### 3. Start Node.js server

```bash id="bqfdcn"
cd api
npm install
node server.js
```

---

### 4. Run frontend

Open this file in your browser:

```bash id="h3zbsy"
public/index.html
```

---

## 🧪 Example

Input:

```id="3m9z7h"
happy
```

Output:

```id="flw0m9"
Pizza, Ice Cream
```

---

## 👨‍💻 Author

Aneri Gupta
