# 🏰 Haunted House: An Interactive Text Adventure

A web-based interactive fiction game built with **FastAPI**, **SQLite**, and vanilla **HTML/CSS/JavaScript**. Navigate through a dark, branching mansion, manage your Sanity, uncover secret rooms, and find your way to safety before madness consumes you.

---

## 🎮 Features

- **Branching Map Architecture:** 10 interconnected rooms featuring choices, secret chambers, traps, and multiple narrative endings.
- **Dynamic Sanity System:** Player Sanity ranges from **0% to 100%**:
  - Traps and eerie rooms decrease Sanity.
  - Safe refuges (e.g., _The Secret Study_) restore Sanity.
  - Dropping to **0% Sanity** triggers an immediate **Game Over** state.
- **Multiple Endings:**
  - **Victory:** Reach the safety of _The Garden of Dawn_.
  - **Madness / Traps:** Perish in the _Ritual Chamber_ or get trapped in the _Collapsed Tunnel_.
- **Seamless Reset:** In-game restart mechanism allowing replayability without hard page refreshes.

---

## 💡 Key Learnings

Building this full-stack project provided practical experience with:

1. **REST API Architecture (FastAPI):**
   - Designed clean endpoints (`GET /api/scenes/{id}`).
   - Configured CORS middleware and leveraged automatic JSON response serialization.

2. **Relational Database Design & Management (SQLite):**
   - Structured relational schemas using Foreign Keys (`scenes` and `choices`).
   - Handled bulk inserts (`executemany`) and practiced secure SQL parameter binding (`?`).
   - Understood database transactions (`conn.commit()`) and resolved data synchronization/state issues.
   - Handled robust cross-platform path resolution using Python's `pathlib.Path`.

3. **Asynchronous Frontend & DOM Manipulation (JavaScript):**
   - Used the modern `Fetch API` with `async/await` to communicate with the backend.
   - Dynamically generated interface elements (choice buttons, narrative texts) based on API payloads.
   - Implemented mathematical clamping (`Math.min` / `Math.max`) to enforce state boundaries.

4. **Version Control & Debugging (Git):**
   - Managed project versions, atomic commits, staging, and terminal debugging workflows.

---

## 🛠️ Tech Stack

- **Backend:** Python 3.10+, [FastAPI](https://fastapi.tiangolo.com/), [Uvicorn](https://www.uvicorn.org/)
- **Database:** SQLite3
- **Frontend:** HTML5, CSS3, JavaScript (Vanilla ES6 Fetch API)

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/Haunted-house.git
cd Haunted-house
```

### 2. Set Up a Virtual Environment

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```powershell
pip install -r requirements.txt
```

### 4. Initialize & Populate the Database

Run the database script to generate `backend/game.db` populated with all 10 rooms and narrative choices:

```powershell
python -m backend.database
```

### 5. Launch the FastAPI Backend

Start the development server with live reload:

```powershell
uvicorn backend.main:app --reload
```

The API will be available at:

- **API Root / Scenes:** `http://127.0.0.1:8000/api/scenes/1`
- **Interactive OpenAPI Docs:** `http://127.0.0.1:8000/docs`

### 6. Launch the Frontend

Open `frontend/index.html` directly in your web browser, or serve it using VS Code's **Live Server** extension.

---

## 🗺️ Map Overview

| ID     | Scene Name              | Sanity Impact | Type                    |
| ------ | ----------------------- | :-----------: | ----------------------- |
| **1**  | The Entrance Hall       |      0%       | Start                   |
| **2**  | The Grand Library       |     -10%      | Exploration             |
| **3**  | The Dining Hall         |      -5%      | Exploration             |
| **4**  | The Damp Basement       |     -25%      | Danger                  |
| **5**  | The Secret Study        |     +15%      | Safe Haven              |
| **6**  | The Sunken Conservatory |     -10%      | Exploration             |
| **7**  | The Wine Cellar         |     -15%      | Exploration             |
| **8**  | The Ritual Chamber      |     -100%     | **Game Over** (Madness) |
| **9**  | The Collapsed Tunnel    |     -100%     | **Game Over** (Trapped) |
| **10** | The Garden of Dawn      |      0%       | **Victory** (Escaped)   |
