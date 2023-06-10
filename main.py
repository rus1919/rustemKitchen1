import asyncio
import random
import sys
import traceback

#import gevent
#from gevent.pywsgi import WSGIServer

from flask import Flask, request, render_template, send_file, flash, redirect
import config
import db_func
from config import path



app = Flask(__name__)
@app.route('/favicon.ico')
def favicon():
    return 'True'
@app.route('/calc/<tlgm_id>', methods=['GET', 'POST'])
def main(tlgm_id):
    rq = request.form
    rand = random.randint(1,44)
    if request.method=='POST':
        print(rq)
        if 'step1' in rq.keys():
            type_kitchen = rq['step1']
            db_func.calc_filler(tlgm_id=tlgm_id,type_kitchen=type_kitchen)
            return render_template('main.html', step=2, type_kitchen =type_kitchen ,rand = rand)

    return render_template('main.html', step=1, rand = rand)

############################


print(path,'path')
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
