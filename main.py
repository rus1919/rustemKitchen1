import random
from flask import Flask, request, render_template
from db_func import calc_filler, get_column_value, get_pict, get_type_verh_skaf
from config import path

app = Flask(__name__)


@app.route('/favicon.ico')
def favicon():
    return 'True'


@app.route('/calc/<tlgm_id>', methods=['GET', 'POST'])
def main(tlgm_id):
    rq = request.form
    rand = random.randint(1, 44)
    if request.method == 'POST':
        print(rq)
        if 'step1' in rq.keys():
            type_kitchen = rq['step1']
            calc_filler(tlgm_id=tlgm_id, column='type_kitchen', value=type_kitchen)
            posudomoika = 3
            oborud = 'Посудомойка'
            header_text = 'Выберите технику для кухни'
            return render_template('main.html', step=2.0, type_kitchen=type_kitchen, rand=rand,
                                   posudomoika=posudomoika, oborud=oborud, header_text=header_text)
        if 'posudomoika' in rq.keys():
            posudomoika = 0
            if rq['posudomoika'] == 'da':
                posudomoika = 1
            oborud = 'Посудомойка'
            header_text = 'Выберите технику для кухни'
            return render_template('main.html', step=2.0, posudomoika=posudomoika, rand=rand, oborud=oborud,
                                   header_text=header_text)
        if 'duhovka' in rq.keys() and 'save' not in rq.keys():
            duhovka = rq['duhovka']
            oborud = 'Духовка'
            pict = get_pict(duhovka=duhovka)
            header_text = 'Выберите технику для кухни'
            return render_template('main.html', step=2.1, duhovka=duhovka, rand=rand, oborud=oborud, pict=pict,
                                   header_text=header_text)
        if 'vitag' in rq.keys() and 'save' not in rq.keys():
            vitag = rq['vitag']
            oborud = 'Вытяжка'
            duhovka = get_column_value(tlgm_id=tlgm_id, column='duhovka')
            pict = get_pict(duhovka=duhovka, vitag=vitag)
            header_text = 'Выберите технику для кухни'
            return render_template('main.html', step=2.2, duhovka=duhovka, vitag=vitag, rand=rand, oborud=oborud,
                                   pict=pict, header_text=header_text)
        if 'micro' in rq.keys() and 'save' not in rq.keys():
            micro = rq['micro']
            oborud = 'Микроволновка'
            duhovka = get_column_value(tlgm_id=tlgm_id, column='duhovka')
            vitag = get_column_value(tlgm_id=tlgm_id, column='vitag')
            pict = get_pict(duhovka=duhovka, vitag=vitag, micro=micro)
            header_text = 'Выберите технику для кухни'
            return render_template('main.html', step=2.3, duhovka=duhovka, vitag=vitag, micro=micro, rand=rand,
                                   oborud=oborud, pict=pict, header_text=header_text)
        if 'holod' in rq.keys() and 'save' not in rq.keys():
            holod = rq['holod']
            oborud = 'Холодильник'
            micro = get_column_value(tlgm_id=tlgm_id, column='micro')
            duhovka = get_column_value(tlgm_id=tlgm_id, column='duhovka')
            vitag = get_column_value(tlgm_id=tlgm_id, column='vitag')
            header_text = 'Выберите технику для кухни'
            pict = get_pict(duhovka=duhovka, vitag=vitag, micro=micro, holod=holod)

            return render_template('main.html', step=2.4, duhovka=duhovka, vitag=vitag, holod=holod, miсro=micro,
                                   rand=rand, oborud=oborud, pict=pict, header_text=header_text)

        if 'save' in rq.keys():
            step = float(rq['save'])
            if step == 2.0:
                oborud = 'Духовка'
                calc_filler(tlgm_id=tlgm_id, column='posud', value=rq['posud'])
                pict = 'shag2/posud/posud-da.webp'
                header_text = 'Выберите технику для кухни'
                return render_template('main.html', step=2.1, rand=rand, oborud=oborud, pict=pict,
                                       header_text=header_text)
            if step == 2.1:
                oborud = 'Вытяжка'
                calc_filler(tlgm_id=tlgm_id, column='duhovka', value=rq['duhovka'])
                duhovka = get_column_value(tlgm_id=tlgm_id, column='duhovka')
                pict = get_pict(duhovka=duhovka)
                header_text = 'Выберите технику для кухни'
                return render_template('main.html', step=2.2, rand=rand, oborud=oborud, duhovka=duhovka, pict=pict,
                                       header_text=header_text)
            if step == 2.2:
                header_text = 'Выберите технику для кухни'
                oborud = 'Микроволновка'
                calc_filler(tlgm_id=tlgm_id, column='vitag', value=rq['vitag'])
                duhovka = get_column_value(tlgm_id=tlgm_id, column='duhovka')
                vitag = get_column_value(tlgm_id=tlgm_id, column='vitag')
                pict = get_pict(duhovka=duhovka, vitag=vitag)
                return render_template('main.html', step=2.3, rand=rand, oborud=oborud, duhovka=duhovka, vitag=vitag,
                                       pict=pict, header_text=header_text)
            if step == 2.3:
                oborud = 'Холодильник'
                calc_filler(tlgm_id=tlgm_id, column='micro', value=rq['micro'])
                duhovka = get_column_value(tlgm_id=tlgm_id, column='duhovka')
                vitag = get_column_value(tlgm_id=tlgm_id, column='vitag')
                micro = get_column_value(tlgm_id=tlgm_id, column='micro')
                pict = get_pict(duhovka=duhovka, vitag=vitag, micro=micro)
                header_text = 'Выберите технику для кухни'
                return render_template('main.html', step=2.4, rand=rand, oborud=oborud, duhovka=duhovka, vitag=vitag,
                                       pict=pict, header_text=header_text)
            if step == 2.4:
                header_text = 'Выберите вид верхних шкафов'
                calc_filler(tlgm_id=tlgm_id, column='holod', value=rq['holod'])
                type_kitchen = get_column_value(tlgm_id=tlgm_id, column='type_kitchen')
                pict = get_pict(type_kitchen=type_kitchen)
                sub_pict = get_type_verh_skaf(type_kitchen)
                print(type_kitchen)
                return render_template('main.html', step=3.0, rand=rand, pict=pict, header_text=header_text,
                                       type_kitchen=type_kitchen,sub_pict=sub_pict)
        if 'back' in rq.keys():
            return render_template('main.html', step=float(rq['back']))
    return render_template('main.html', step=1, rand=rand)


############################


print(path, 'path')
cert = path + 'cert/incyprus_pro.crt'
key = path + 'cert/incyprus_pro.key'
if __name__ == '__main__':
    app.run(host='0.0.0.0', ssl_context=(cert, key), port=443, debug=True)
"""https_server = WSGIServer(('0.0.0.0', 443), app, keyfile=key, certfile=cert)
https_server.start()

http_server = WSGIServer(('0.0.0.0', 80), app)
http_server.start()

while True:
    gevent.sleep(60)"""
