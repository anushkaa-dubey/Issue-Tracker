from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import issues

app = FastAPI(title="Issue Tracker API", version="1.0.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # Angular dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(issues.router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "Issue Tracker API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)