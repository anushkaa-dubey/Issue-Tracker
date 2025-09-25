
# Issue Tracker

A full-stack issue tracking application with a Python FastAPI backend and an Angular frontend.

---

## Assignment Requirements

**Assignment: Build a Small Issue Tracker**

Develop a simple Issue Tracker with a Python backend serving REST APIs and an Angular frontend with a functional UI. The system should allow users to view, search, filter, sort, create, and update issues.

### Part 1: Backend (Python)
#### Endpoints
- `GET /health` → `{ "status": "ok" }`
- `GET /issues` → Supports search by title, filters, sorting, and pagination (`page`, `pageSize`).
- `GET /issues/:id` → Return single issue.
- `POST /issues` → Create new issue. The backend should auto-generate `id`, add `createdAt` and `updatedAt`.
- `PUT /issues/:id` → Update issue. The `updatedAt` field should be refreshed.

### Part 2: Frontend (Angular)
#### Requirements
- **Issues List Page**
   - Display a table with columns: `id`, `title`, `status`, `priority`, `assignee`, and `updatedAt`.
   - Provide filters for status, priority, and assignee.
   - Implement a search box.
   - Enable sorting.
   - Support pagination with `page` and `pageSize`.
   - Include action buttons: Create Issue (opens a form to add a new issue), and Edit Issue (update issue details).
   - Clicking a row (except Edit) opens the Issue Detail view.
- **Issue Detail Page**
   - Show the full issue JSON in a drawer or a separate route.

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
