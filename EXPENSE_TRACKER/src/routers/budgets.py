
from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
import crud
from database import get_db
import shema


router=APIRouter(prefix="/api/budgets",tags=["budgets"])

@router.post("/",response_model=shema.budget_Response,tags=["budgets add"])
def add_budgets(shema:shema.budgetCreate,db:Session=Depends(get_db)):
    return crud.create_budgets(db=db,shema=shema)

@router.put("/{id}",response_model=shema.budget_Response,tags=["update budgets"])
def update_budgets(shema:shema.budgetCreate,id:int,db:Session=Depends(get_db)):
    return crud.budgets_update(shema,db,id)

@router.get("/all/",response_model=list[shema.budget_Response],tags=["get all budgets"])
def get_all_budgets(limit=3,offset=0,db:Session=Depends(get_db)):
    return crud.get_all_budgets(db,limit,offset)

@router.get("/budgetsbyId/{id}",response_model=shema.budget_Response,tags=["get budgets byID"])
def get_byId_budgets(id:int,db:Session=Depends(get_db)):
    return crud.get_budgets_byID(id,db)

@router.delete("/delete_byId/{id}",response_model=shema.budget_Response,tags=["delete budgets by ID"])
def delete_budgets(id,db:Session=Depends(get_db)):
    return crud.delete_budgets_byID(id,db)






