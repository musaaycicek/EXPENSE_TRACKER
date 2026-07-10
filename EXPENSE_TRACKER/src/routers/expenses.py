
from fastapi import APIRouter,HTTPException,Depends
from sqlalchemy.orm import Session
from datetime import datetime
import crud
from database import get_db
import shema



router=APIRouter(prefix="/api/expenses",tags=["Expenses"])


@router.post("/",response_model=shema.income_Response,tags=["expenses post"])
def add_expenses(income_data:shema.expensesCreate,db:Session=Depends(get_db)):
   
  return crud.expenses_add(db=db,shema=income_data)


@router.get("/all/",response_model=list[shema.income_Response],tags=["expenses get all"])
def get_All_expense(offset:int=0,limit:int=10,db:Session=Depends(get_db)):
 return crud.get_all_expenses(db=db,offset=offset,limit=limit)


@router.get("/getByID/{id}",response_model=shema.expenses_Response,tags=["expenses get by Id"])
def get_byID_expense(id:int,db:Session=Depends(get_db)):
 return crud.get_expenses_byId(id,db=db)

@router.delete("/deleteByID/{id}",response_model=shema.expenses_Response,tags=["expenses delete by Id"])
def delete_byID_expense(id,db:Session=Depends(get_db)):
  return crud.delete_expenses_byID(id=id,db=db)
