# Todo App (FastAPI + SQLite)

Simple Todo application with a FastAPI backend and vanilla HTML/CSS/JS frontend.

## Quickstart

1. Create and activate venv (optional)
```bash
python -m venv .venv && source .venv/bin/activate
```
2. Install dependencies
```bash
pip install -r requirements.txt
```
3. Run the server
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```
4. Open the app

Visit http://localhost:8000 in your browser.

## Structure

```
workspace/
  app/
    main.py
    db.py
    models.py
    schemas.py
    crud.py
    routers/
      todos.py
    static/
      index.html
      styles.css
      app.js
  requirements.txt
  README.md
```

