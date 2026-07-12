

from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
import crud
from database import get_db
import shema
import model


router=APIRouter(prefix="/api/incomes",tags=["Incomes"])

@router.post("/",response_model=shema.income_Response,tags=["incomes post"])
def add_incomes(shema:shema.incomeCreate,db:Session=Depends(get_db)):
    return crud.expenses_add(db=db,shema=shema)

@router.put("/{id}",response_model=shema.income_Response,tags=["incomes update"])
def update_income(id:int,upt_shema:shema.incomeCreate,db:Session=Depends(get_db)):
    return crud.update_income(id,upt_shema,db)

@router.get("/all/",response_model=list[shema.income_Response],tags=["incomes get all"])
def get_all_income(db:Session=Depends(get_db),offset=0,limit=3):
    return crud.get_all_income(db,offset,limit)

@router.get("/getById/{id}",response_model=shema.income_Response,tags=["incomes get by Id"])
def get_Id_incomes(id:int,db:Session=Depends(get_db)):
    return crud.get_expenses_byId(id,db)

@router.delete("/deleteByID",response_model=shema.income_Response,tags=["incomes delete"])
def delete(id:int,db:Session=Depends(get_db)):
    return crud.delete_expenses_byID(id,db)
