from flask import Flask, make_response, request
import requests
import time

app = Flask(__name__, static_url_path='/')

@app.route('/')
def load():
    response = make_response(open('./download_test.html').read())
    # data_base_query()
    return response

@app.route('/data')
def data_return():
    print(request.args)
    print("%(year)s-%(month)s-%(day)s" % request.args)
    print('oh snap at', time.time())
    text_response = data_base_query()
    print(type(text_response), 'at', time.time())
    print(text_response[0:200])
    # return 'poot'
    return data_base_query()

def data_base_query():
    endpoint ="https://omniweb.sci.gsfc.nasa.gov/cgi/nx1.cgi"
    options = {
        'activity': 'retrieve',
        'sars': '4',
        'res': 'min',
        'spacecraft':'sc_merge_min',
        'num_plot':'1',
        'start_date':'20180207',
        'end_date':'20180208',
        'vars':'11',
        'scale':'Linear',
        'xstyle':'0',
        'ystyle':'0',
        'symbol':'0',
        'imagex':'640',
        'imagey':'480'
    }
    r = requests.post(endpoint, data=options)
    # print(r)
    # print(r.text)
    return r.text
