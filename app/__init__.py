from flask import Flask, make_response, request
import requests
import time
import datetime

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
    text_response = data_base_query(
        year=int(request.args['year']),
        month=int(request.args['month']),
        day=int(request.args['day'])
        )
    print(type(text_response), 'at', time.time())
    print(text_response[0:200])
    # return 'poot'
    return text_response

def data_base_query(year,month,day):
    query_date = datetime.datetime(year=year,month=month,day=day)
    two_days = datetime.timedelta(days=2)
    start_date = query_date-two_days
    print(datetime_object_to_str(start_date))
    print(datetime_object_to_str(query_date))
    endpoint ="https://omniweb.sci.gsfc.nasa.gov/cgi/nx1.cgi"
    options = {
        'activity': 'retrieve',
        'sars': '4',
        'res': 'min',
        'spacecraft':'sc_merge_min',
        'num_plot':'1',
        'start_date':datetime_object_to_str(start_date),
        'end_date':datetime_object_to_str(query_date),
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

def datetime_object_to_str(date_obj):
    return "%04d%02d%02d"%(date_obj.year, date_obj.month,date_obj.day)
