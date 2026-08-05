from fastapi import APIRouter,Depends,HTTPException,status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database import get_db
import model
import EXPENSE_TRACKER.src.security as security

router=APIRouter(prefix="/auth",tags=["Authentication"])
@router.post("/login")
def login(form_data:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    user=db.query(model.User).filter(model.User.email==form_data.username).first()

    if not user or not security.verified_password(form_data.password,user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,detail="E-posta veya şifre hatalı")

                            
    access_token=security.create_access_token(
        data={"sub":str(user.id),"email":user.email}
    )

    return {"access_token":access_token,"token_type":"bearer"}


