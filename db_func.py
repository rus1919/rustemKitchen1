import datetime
import sqlite3
from config import db_path


def new_user(tlgm_id, user_name):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    sql = f'select * from users where tlgm_id={tlgm_id}'
    cursor.execute(sql)
    if cursor.fetchone() == None:
        sql = 'insert into users (tlgm_id,user_name,date_reg) values (?,?,?)'
        date_reg = str(datetime.datetime.now().replace(microsecond=0))
        cursor.execute(sql, (tlgm_id, user_name, date_reg))
    conn.commit()


def calc_filler(tlgm_id, column, value):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    sql = f"select * from orders where tlgm_id={tlgm_id}"
    cursor.execute(sql)
    if cursor.fetchone() == None:
        sql = "insert into orders (tlgm_id,type_kitchen) values (?,?)"
        cursor.execute(sql, (tlgm_id, value))
    else:
        if column == 'type_kitchen':
            sql = f"update orders set {column}='{value}' where tlgm_id={tlgm_id}"
        else:
            sql = f"update orders set {column}='{value}' where tlgm_id={tlgm_id}"
        cursor.execute(sql)

    conn.commit()


def get_column_value(tlgm_id, column):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    sql = f"select {column} from orders where tlgm_id={tlgm_id}"
    cursor.execute(sql)
    return cursor.fetchone()[0]


def get_pict(duhovka=None, vitag=None, micro=None, holod=None, type_kitchen=None):
    res = f'shag2/duhovka/duh-{duhovka}.webp'
    if vitag != None:
        res = f'shag2/vitag/duh-{duhovka}_vitag-{vitag}.webp'
        if micro != None:
            res = f'shag2/micro/duh-{duhovka}_vitag-{vitag}_micro-{micro}.webp'
            if holod != None:
                res = f'shag2/holod/duh-{duhovka}_vitag-{vitag}_micro-{micro}_holod-{holod}.webp'
    if type_kitchen == 'premaya':
        res = 'shag3/pr/shkaf_zastavka.webp'
    if type_kitchen == 'uglovaya_levaya':
        res = 'shag3/ugl/zastavk.webp'
    if type_kitchen == 'uglovaya_pravaya':
        res = 'shag3/ugl/zastavk.webp'
    if type_kitchen == 'p_obraznaya':
        res = 'shag3/pobraz/zastav.webp'

    return res


def get_type_verh_skaf(type_kitchen):
    d = {
        'uglovaya_levaya': {'pict1_1': {'path':'/static/img/calc/shag3/ugl/bez_verh.webp','text':'Без верха'},
                            'pict1_2': {'path':'/static/img/calc/shag3/ugl/verh a.webp','text':'Верх A'},
                            'pict2_1': {'path':'/static/img/calc/shag3/ugl/verh_a_b.webp','text':'Верх А-B'},
                            'pict2_2': {'path':'/static/img/calc/shag3/ugl/verh_b.webp','text':'Верх B'}
                            },
        'uglovaya_pravaya': {'pict1_1': {'path':'/static/img/calc/shag3/ugl/bez_verh.webp','text':'Без верха'},
                             'pict1_2': {'path':'/static/img/calc/shag3/ugl/verh a.webp','text':'Верх A'},
                             'pict2_1': {'path':'/static/img/calc/shag3/ugl/verh_a_b.webp','text':'Верх A-B'},
                             'pict2_2': {'path':'/static/img/calc/shag3/ugl/verh_b.webp','text':'Верх B'}
                             },
        'p_obraznaya': {'pict1_1': {'path':'/static/img/calc/shag3/pobraz/bez_verh.webp','text':'Без верха'},
                        'pict1_2': {'path':'/static/img/calc/shag3/pobraz/verh_a.webp','text':'Верх A'},
                        'pict2_1': {'path':'/static/img/calc/shag3/pobraz/verh_a_b.webp','text':'Верх A-B'},
                        'pict2_2': {'path':'/static/img/calc/shag3/pobraz/verh_a_b_c.webp','text':'Верх A-B-C'},
                        'pict3_1': {'path':'/static/img/calc/shag3/pobraz/verh_b.webp','text':'Верх B'},
                        'pict3_3': {'path':'/static/img/calc/shag3/pobraz/verh_b_c.webp','text':'Верх B-C'},
                        'pict4_1': {'path':'/static/img/calc/shag3/pobraz/verh_c.webp','text':'Верх C'}
                        },
        'premaya': {'pict1_1': {'path':'/static/img/calc/shag3/pr/s_antresol.webp','text':'С антресолью'},
                    'pict1_2': {'path':'/static/img/calc/shag3/pr/s_glubokoi antresol.webp','text':'С глубокой антресолью'},
                    'pict2_1': {'path':'/static/img/calc/shag3/pr/standart.webp','text':'Стандарт'},
                    'pict2_2': {'path':'/static/img/calc/shag3/pr/visokii.webp','text':'Высокий'}
                    },
    }
    return d[type_kitchen]
