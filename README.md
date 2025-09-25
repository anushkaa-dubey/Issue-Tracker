
# Issue Tracker

A full-stack issue tracking application with a Python FastAPI backend and an Angular frontend.

---


## Project Goals

This project is a simple Issue Tracker built with a Python FastAPI backend and an Angular frontend. The main goals are:

- Provide a REST API for managing issues, including viewing, searching, filtering, sorting, creating, and updating issues.
- Deliver a modern Angular UI for interacting with the issue tracker, supporting all core features.

### Backend (Python/FastAPI)
Implements endpoints:
- `GET /health` — Health check
- `GET /issues` — List issues, with search (by title), filters, sorting, and pagination (`page`, `pageSize`)
- `GET /issues/:id` — Get a single issue
- `POST /issues` — Create a new issue (auto-generates `id`, adds `createdAt` and `updatedAt`)
- `PUT /issues/:id` — Update an issue (refreshes `updatedAt`)

### Frontend (Angular)
Features:
- Issues List Page: Table view with columns (`id`, `title`, `status`, `priority`, `assignee`, `updatedAt`), filters, search, sorting, pagination, create/edit actions, and row click for detail view
- Issue Detail Page: Shows full issue JSON in a drawer or separate route

---

## Features
- Create, view, update, and delete issues
- RESTful API backend (FastAPI)
- Modern Angular frontend
- Persistent storage (SQLite or other DB)

## Project Structure

```
issue-tracker-backend/   # FastAPI backend
   app/
      main.py             # FastAPI entrypoint
      models.py           # SQLAlchemy models
      database.py         # DB connection
      routers/            # API routes
   requirements.txt      # Python dependencies

issue-tracker-frontend/ # Angular frontend
   src/
      app/
         components/       # Angular components
         models/           # TypeScript models
         services/         # API services
   package.json          # Node dependencies
```

## Getting Started

### Backend (FastAPI)
1. Navigate to `issue-tracker-backend`
2. Create a virtual environment and activate it:
    ```
    python -m venv venv
    venv\Scripts\activate  # On Windows
    source venv/bin/activate  # On Mac/Linux
    ```
3. Install dependencies:
    ```
    pip install -r requirements.txt
    ```
4. Run the server:
    ```
    uvicorn app.main:app --reload
    ```

### Frontend (Angular)
1. Navigate to `issue-tracker-frontend`
2. Install dependencies:
    ```
    npm install
    ```
3. Run the Angular app:
    ```
    npm start
    ```

## API Endpoints
See FastAPI docs at `http://localhost:8000/docs` when backend is running.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](LICENSE)
