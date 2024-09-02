from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models,schemas
import crud
from database import engine,SessionLocal,Base

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_byemail(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already exists")
    return crud.create_user(db=db, user=user)

@app.get("/users/")
def read_users(db:Session = Depends(get_db),skip: int=0,limit: int=100):
    users =  crud.get_user(db=db, skip=skip, limit=limit)
    return users

@app.put("/users/{id}")
def update_user(user:schemas.UserCreate,id:int, db:Session = Depends(get_db)):
    db_user = crud.update_user(db=db,_id=id,user_update=user)
    return db_user

@app.delete("/users/{id}")
def delete_user(id:int, db:Session = Depends(get_db)):
    return crud.delete_user(db=db,_id=id)


@app.post("/users/{user_id}/items", response_model=schemas.Item)
def create_items(user_id:int, item: schemas.ItemCreate, db:Session = Depends(get_db)):
    return crud.create_item(db=db, user_id=user_id, item=item)

@app.get("/users/{user_id}/items", response_model=list[schemas.Item])
def read_items(skip: int=0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_items(db=db, skip=skip, limit=limit)



