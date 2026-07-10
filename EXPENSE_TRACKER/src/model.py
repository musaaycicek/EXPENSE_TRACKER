
from sqlalchemy.orm import Mapped,mapped_column
from database import Base
from sqlalchemy import DateTime
from sqlalchemy.types import Numeric,String
from datetime import datetime,timezone


class incomes(Base):

    __tablename__="income"

    id:Mapped[int]=mapped_column(primary_key=True,index=True)
    amount:Mapped[float]=mapped_column(Numeric(10,2),nullable=False)
    category:Mapped[str]=mapped_column(String(50),nullable=False)
    description:Mapped[str]=mapped_column(String(255),nullable=True)
    date:Mapped[datetime]=mapped_column(DateTime,default=lambda:datetime.now(timezone.utc))



class expenses(Base):
    __tablename__="expenses"
    
    id:Mapped[int]=mapped_column(primary_key=True,index=True)
    amount:Mapped[float]=mapped_column(Numeric(10,2),nullable=False)
    category:Mapped[str]=mapped_column(String(50),nullable=False)
    description:Mapped[str]=mapped_column(String(255),nullable=True)
    date:Mapped[datetime]=mapped_column(DateTime,default=lambda:datetime.now(timezone.utc))


class budgets(Base):
    __tablename__="budgets"

    id:Mapped[int]=mapped_column(primary_key=True,index=True)
    category:Mapped[str]=mapped_column(String(50),nullable=False)
    amount_limit:Mapped[float]=mapped_column(Numeric(10,2),nullable=False)