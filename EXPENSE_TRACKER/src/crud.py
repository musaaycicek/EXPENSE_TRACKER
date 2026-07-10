import model
import shema
from sqlalchemy.orm import Session



""" INCOME TABLOSU """

# income tablosu için insert işlemi

def incomes_add(db:Session,shema=shema.incomeCreate):
    add_db=model.incomes(amount=shema.amount,
            category=shema.category,
            description=shema.description)
    db.add(add_db)
    db.commit()
    """
        db.refresh() fonksiyonu, veritabanının otomatik ürettiği değerleri (özellikle id sütununu)
          Python nesnemize geri yüklemek ve onu güncellemek için kullanılır.
    """
    db.refresh(add_db)

    return add_db

# income tablosu için update
"""
 update işleminde çevirdiğimiz sorgu ile  shema.Sütun Adlarını ekleriz   
"""
def update_income(id:int,db:Session,shema:shema.incomeCreate):
    # İşlem yapacağımız alan
    db_income_update=db.query(model.incomes).filter(model.incomes.id==id).first()

    # model.incomes.amount=shema.amount
    
    db_income_update.amount=shema.amount
    db_income_update.category=shema.category
    db_income_update.description=shema.description

    db.commit()
    db.refresh(db_income_update)

    return db_income_update


# Tüm veriyi getir
def get_all_income(db:Session,offset=0,limit=3,):
# Burada query içine aranacak alanı yazmamız gerek
    db_all=db.query(model.incomes).offset(offset).limit(limit).all()
    return db_all

# id ile istenen veriyi getir
def get_income_byId(id:int,db:Session):
    db_getID=db.query(model.incomes).filter(model.incomes.id==id).first()
    return db_getID

# income için silme işlemi yapıcam
def delete_income_byID(id:int,db:Session):
    db_delete=db.query(model.incomes).filter(model.incomes.id==id).first()
    
    if db_delete is None:
     return False
    
    db.delete(db_delete)
    
    db.commit()

   

    return True
    

""" Expenses Tablosu """



# expenses tablosu için insert işlemi

def expenses_add(db:Session,shema=shema.expensesCreate):
    add_db=model.expenses(amount=shema.amount,
            category=shema.category,
            description=shema.description)
    db.add(add_db)
    db.commit()
    db.refresh(add_db)

    return add_db

# Tüm veriyi getir
def get_all_expenses(db:Session,offset=0,limit=3,):
# Burada query içine aranacak alanı yazmamız gerek
    db_all=db.query(model.expenses).offset(offset).limit(limit).all()
    return db_all

# id ile istenen veriyi getir
def get_expenses_byId(id:int,db:Session):
    db_getID=db.query(model.expenses).filter(model.expenses.id==id).first()
    return db_getID

# expenses için silme işlemi yapıcam
def delete_expenses_byID(id:int,db:Session):
    db_delete=db.query(model.expenses).filter(model.expenses.id==id).first()
    
    if db_delete is None:
        return False

    db.delete(db_delete)
    
    db.commit()

  
    return True


""" Budgets Tablosu """

def create_budgets(db:Session,shema:shema.budgetCreate):
    db_budget=model.budgets(category=shema.category,amount_limit=shema.amount_limit)
    db.add(db_budget)
    db.commit()
    db.refresh(db_budget)

    return db_budget

# Tüm budgets değerlerini
def get_all_budgets(db:Session,offset=0,limit=3):
    db_all=db.query(model.budgets).offset(offset).limit(limit).all()
    """
    # String donen mesajlar Fastapi de patlar sadece return kullanalım
    # boş değer olursa [] ya da None döner
    if not db_all:
        return "Veri eksik"
    else:
        return db_all
    """
    return db_all

# id ile tüm budgets değerlerini getir
def get_budgets_byID(id:int,db:Session):
    
    db_id=db.query(model.budgets).filter(model.budgets.id==id).first()
    
    return db_id

def delete_budgets_byID(id:int,db:Session):
    db_delete=db.query(model.budgets).filter(model.budgets.id==id).first()

    
    db.delete(db_delete)
    db.commit() 
       
    return db_delete


