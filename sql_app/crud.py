from sqlalchemy.orm import Session
import models, schemas
from exceptions import UserNotFoundError
def get_user(db:Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def get_user_by_id(db:Session,_id:int):
    user = db.query(models.User).get(_id)

    if user is None:
        raise UserNotFoundError

    return user

def get_user_byemail(db:Session, email : str):
    return db.query(models.User).filter(models.User.email==email).first()

def create_user(db:Session, user:schemas.UserCreate):
    hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email,hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db:Session, _id:int, user_update: schemas.UserCreate):
    user = get_user_by_id(db,_id)

    if user is None:
        raise UserNotFoundError

    hashed_password = user_update.password + "notreallyhashed"
    user.hashed_password = hashed_password
    user.email = user_update.email

    db.commit()
    db.refresh(user)

    return user;

def delete_user(db:Session, _id:int):
    user = get_user_by_id(db,_id)

    if user is None:
        raise UserNotFoundError

    db.delete(user)
    db.commit()

    return




def get_items(db:Session,skip:int=0,limit:int=100):
    return db.query(models.Item).offset(skip).limit(limit).all()

def create_item(db:Session,item:schemas.ItemCreate, user_id:int):
    db_item = models.Item(**item.dict(),owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

