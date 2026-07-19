
# EmailStr yeni eklendi
from pydantic import BaseModel,EmailStr
from datetime import datetime


class incomeBase(BaseModel):
    amount:int
    category:str
    description:str

class incomeCreate(incomeBase):pass

class income_Response(incomeBase):
    id:int
    date:datetime

    class Config:
        from_attributes = True


class expensesBase(BaseModel):
    amount:int
    category:str
    description:str

class expensesCreate(expensesBase):pass

class expenses_Response(expensesBase):
    id:int
    date:datetime | None

    class Config:
        from_attributes = True


class budgetsBase(BaseModel):
    category:str
    amount_limit:float

class budgetCreate(budgetsBase):pass

class budget_Response(budgetsBase):
    id:int
    class Config:
        from_attributes=True


# User için şema oluşturmamız lazım  
# Yeni bir veri tipi kullanmamız lazım EmailStr ->  pip install email-validator
# password kısmını userbase içine yazarsak Response da şifre görünür

class UserBase(BaseModel):
    email:str
    

class UserCreate(UserBase):
    password:str 

class User_Response(UserBase): 
    id:int
    date_created:datetime | None

    class Config:
        from_attributes=True

