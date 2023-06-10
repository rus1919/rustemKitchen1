import datetime
import sqlite3
from config import db_path
def new_user(tlgm_id,user_name):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    sql = f'select * from users where tlgm_id={tlgm_id}'
    cursor.execute(sql)
    if cursor.fetchone()==None:
        sql = 'insert into users (tlgm_id,user_name,date_reg) values (?,?,?)'
        date_reg = str(datetime.datetime.now().replace(microsecond=0))
        cursor.execute(sql,(tlgm_id,user_name,date_reg))
    conn.commit()
def calc_filler(tlgm_id,type_kitchen=None,column=None,value=None):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    sql = f"select * from orders where tlgm_id={tlgm_id}"
    cursor.execute(sql)
    if cursor.fetchone()==None:
        sql = "insert into orders (tlgm_id,type_kitchen) values (?,?)"
        cursor.execute(sql,(tlgm_id,type_kitchen))
    else:
        if column!=None:
            sql = f"update orders set {column}='{value}' where tlgm_id={tlgm_id}"
            cursor.execute(sql)
    conn.commit()
