
from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from database import get_db
import shema
import crud
import model


router=APIRouter(tags=["Users"])

@router.post("/signup",response_model=shema.User_Response,status_code=status.HTTP_201_CREATED)
def signup(user_data:shema.UserCreate,db:Session=Depends(get_db)):
    db_user=db.query(model.User).filter(model.User.email==user_data.email).first()

    return crud.create_user(db,db_user)
 





