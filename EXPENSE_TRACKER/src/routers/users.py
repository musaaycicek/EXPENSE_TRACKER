from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
import model
import shema
import EXPENSE_TRACKER.src.security as security
from crud import create_user


router=APIRouter(prefix="/users",tags=["Users"])

#Kayıt olma(sign-up)
@router.post("/",status_code=status.HTTP_201_CREATED,response_model=shema.User_Response)
def create_user(user_data:shema.UserCreate,db:Session=Depends(get_db)):
    existing_user=create_user(db,user_data)

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="bu e-posta zaten kullanılıyor"
        )
    return existing_user

# Kendi Profilini Görme
@router.get("/me", response_model=shema.UserResponse)
def get_my_profile(current_user: model.User = Depends(security.get_current_user)):
    return current_user

