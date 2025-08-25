from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from .routers import todos as todos_router


app = FastAPI(title="Todo App")

# CORS for local usage and simple deployments
app.add_middleware(
	CORSMiddleware,
	allow_origins=["*"],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)

@app.get("/health")
def health() -> dict:
	return {"status": "ok"}

app.include_router(todos_router.router, prefix="/api/todos", tags=["todos"])

# Serve static frontend
app.mount("/", StaticFiles(directory="app/static", html=True), name="static")

