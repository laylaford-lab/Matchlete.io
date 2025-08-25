from sqlalchemy.orm import Session
from . import models, schemas


def create_todo(db: Session, todo_in: schemas.TodoCreate) -> models.Todo:
	todo = models.Todo(
		title=todo_in.title,
		description=todo_in.description,
		is_done=todo_in.is_done,
	)
	db.add(todo)
	db.commit()
	db.refresh(todo)
	return todo


def list_todos(db: Session, skip: int = 0, limit: int = 100) -> list[models.Todo]:
	return db.query(models.Todo).offset(skip).limit(limit).all()


def get_todo(db: Session, todo_id: int) -> models.Todo | None:
	return db.query(models.Todo).filter(models.Todo.id == todo_id).first()


def update_todo(db: Session, todo_id: int, todo_in: schemas.TodoUpdate) -> models.Todo | None:
	todo = get_todo(db, todo_id)
	if not todo:
		return None
	update_data = todo_in.model_dump(exclude_unset=True)
	for key, value in update_data.items():
		setattr(todo, key, value)
	db.add(todo)
	db.commit()
	db.refresh(todo)
	return todo


def delete_todo(db: Session, todo_id: int) -> bool:
	todo = get_todo(db, todo_id)
	if not todo:
		return False
	db.delete(todo)
	db.commit()
	return True

