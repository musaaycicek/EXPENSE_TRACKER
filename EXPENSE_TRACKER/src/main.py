from fastapi import FastAPI

from routers.expenses import router as expenses_router
from routers.incomes import router as incomes_router

from database import engine
import model

app=FastAPI()



app.include_router(expenses_router)
app.include_router(incomes_router)







