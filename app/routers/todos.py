from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from .. import crud, schemas, models
from ..db import Base, engine, get_db


# Ensure tables exist at import time
Base.metadata.create_all(bind=engine)

router = APIRouter()


@router.get("/", response_model=list[schemas.TodoOut])
def api_list_todos(
	db: Session = Depends(get_db), skip: int = Query(0, ge=0), limit: int = Query(100, ge=1, le=500)
):
	return crud.list_todos(db, skip=skip, limit=limit)


@router.post("/", response_model=schemas.TodoOut, status_code=status.HTTP_201_CREATED)
def api_create_todo(todo_in: schemas.TodoCreate, db: Session = Depends(get_db)):
	return crud.create_todo(db, todo_in)


@router.get("/{todo_id}", response_model=schemas.TodoOut)
def api_get_todo(todo_id: int, db: Session = Depends(get_db)):
	todo = crud.get_todo(db, todo_id)
	if not todo:
		raise HTTPException(status_code=404, detail="Todo not found")
	return todo


@router.patch("/{todo_id}", response_model=schemas.TodoOut)
def api_update_todo(todo_id: int, todo_in: schemas.TodoUpdate, db: Session = Depends(get_db)):
	todo = crud.update_todo(db, todo_id, todo_in)
	if not todo:
		raise HTTPException(status_code=404, detail="Todo not found")
	return todo


@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def api_delete_todo(todo_id: int, db: Session = Depends(get_db)):
	success = crud.delete_todo(db, todo_id)
	if not success:
		raise HTTPException(status_code=404, detail="Todo not found")
	return None

