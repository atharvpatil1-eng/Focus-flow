# FocusFlow

FocusFlow is a modern, full-stack productivity application designed to help you manage tasks efficiently using the Kanban method and stay focused with a built-in Pomodoro timer.

## Features

*   **Kanban Board:** Organize tasks into "To Do", "In Progress", and "Done" columns.
*   **Drag & Drop:** Seamlessly move tasks between columns with a smooth drag-and-drop interface.
*   **Pomodoro Timer:** Boost productivity with a 25-minute focus timer and break intervals.
*   **Real-time Updates:** Changes are instantly saved to the database.
*   **Responsive Design:** Works beautifully on desktop and mobile.

## Tech Stack

This project uses a modern, industry-standard tech stack that demonstrates full-stack development skills:

### Backend
*   **Python (FastAPI):** High-performance, modern web framework for building APIs.
*   **SQLAlchemy:** The Python SQL toolkit and Object Relational Mapper (ORM).
*   **Pydantic:** Data validation and settings management using Python type hints.
*   **SQLite:** Lightweight, serverless database engine (great for portability).

### Frontend
*   **React:** The most popular JavaScript library for building user interfaces.
*   **Vite:** Next-generation frontend tooling for ultra-fast development.
*   **Tailwind CSS:** A utility-first CSS framework for rapid UI development.
*   **@hello-pangea/dnd:** A library for accessible drag-and-drop interfaces in React.
*   **Axios:** Promise-based HTTP client for the browser.

## Getting Started

### Prerequisites

*   **Python 3.8+**
*   **Node.js 16+**

### Installation & Run

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/focusflow.git
    cd focusflow
    ```

2.  **Run the application:**
    We have included a convenient script to start both the backend and frontend servers with a single command:
    ```bash
    ./run.sh
    ```

    *   The **Backend API** will start at `http://localhost:8000`
    *   The **Frontend App** will start at `http://localhost:5173`

### Manual Setup (Optional)

If you prefer to run services manually:

**Backend:**
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

**Frontend:**
```bash
cd frontend
npm install
npm run dev
```

## Project Structure

```
focusflow/
├── backend/            # FastAPI Backend
│   ├── main.py         # App entry point
│   ├── models.py       # Database models
│   ├── schemas.py      # Pydantic schemas
│   ├── crud.py         # Database operations
│   ├── database.py     # DB connection
│   └── requirements.txt
├── frontend/           # React Frontend
│   ├── src/
│   │   ├── components/ # React components (TaskBoard, PomodoroTimer)
│   │   ├── App.jsx     # Main application component
│   │   └── index.css   # Global styles (Tailwind)
│   └── package.json
└── run.sh              # Startup script
```

## Future Improvements

*   User Authentication (Login/Register)
*   Task Categories/Tags
*   Data Visualization (Charts for completed tasks)
*   Dark Mode

---

Built by Atharv Patil
