from fastapi import FastAPI

from routers.expenses import router as expenses_router
from routers.incomes import router as incomes_router
from routers.budgets import router as budgets_router

from database import engine
import model

model.Base.metadata.create_all(bind=engine)

app=FastAPI(
    title= "Expenses Tracker",
    description="Fast API Expenses Tracker",
    version="1.0.0"
)



app.include_router(expenses_router,prefix="/api/expenses")
app.include_router(incomes_router,prefix="/api/incomes")
app.include_router(budgets_router,prefix="/api/budgets")



@app.get("/",tags=["Root"])
def read_root():
    return {"message": "Harcama ve Gelir Takip API'sine Hoş Geldin Musa!"}





