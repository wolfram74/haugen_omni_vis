from flask import Flask, make_response, request
import requests

app = Flask(__name__, static_url_path='/')

@app.route('/')
def load():
    response = make_response(open('./download_test.html').read())
    # data_base_query()
    return response
