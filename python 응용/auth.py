# fast api 및 uvicorn 서버
from fastapi import FastAPI
import uvicorn
# DB 통신 설정, sqlachemy
# from sqlalchemy import create_engine, Table, MetaData, select
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.orm import declarative_base

# import pymysql
# from pydantic import BaseModel, HttpUrl


# class RecipeBase(BaseModel):
#     auth_standard_img_id: int
#     standard_img: HttpUrl
#     participation_id: int


# SQL Enzine 설정
# SQLALCHEMY_DATABASE_URL = "mysql+pymysql://ollenge:ollenge1010@localhost:3306/ollenge"

# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, pool_pre_ping=True, pool_size=15, max_overflow=0, encoding='utf8', convert_unicode=True
# )
# metadata_obj = MetaData(bind=engine)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# db = SessionLocal()
# tata = Table("auth_standard_img", metadata_obj, autoload_with=engine)
# stmt = select(tata)
# datas = db.execute(stmt)
# # print(len(datas))
# for data in datas:
#     print(1)
#     print(data.standard_img)

import pymysql
import os


def get_connection():
    return pymysql.connect(
        user = "ollenge",
        password = 'ollenge1010',
        host = 'localhost',
        port = 3306,
        db = "ollenge",
        charset = 'utf8'
    )


def execute_select(sql):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result


def execute_insert_many(sql):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()


def execute_delete():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM user')
    conn.commit()
    cursor.close()
    conn.close()

def select_news():
    sql = "SELECT * from user"
    return execute_select(sql)


def insert_news():
    sql = "INSERT INTO user (auth_code, login_type, nickname, profile_img, user_description, user_score) VALUES ('ABAB', 'kaka', 'dheldh', 'srl', 'des', 77);"
    execute_insert_many(sql)

# execute_delete()
insert_news()
print(select_news())

# 앱 시작
app = FastAPI()

@app.get("/")
async def root():
    memos = db.query(User).all()
    return {"message": memos}


@app.get("/hello/{name}")
async def say_hello(name: str):
    memos = db.query(User).all()
    return {"message": memos}



# reload app
if __name__ == '__main__':
    uvicorn.run("auth:app", host="localhost:8080", port=80, reload=True)