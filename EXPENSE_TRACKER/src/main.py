from fastapi import FastAPI

from routers.expenses import router as expenses_router

from database import engine
import model

app=FastAPI()



app.include_router(expenses_router)







