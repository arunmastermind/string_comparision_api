#!/usr/local/bin/python
# coding=utf8

from stringFuzzer import failureMatcher
from flask import Flask, render_template, Markup, request, jsonify
# from urllib import unquote
import difflib
# import urllib
from urllib.parse import unquote
app = Flask(__name__)

differ = difflib.HtmlDiff(tabsize=20, wrapcolumn=50)
# differ._legend = ''

@app.route('/', defaults={'str1':'test', 'str2':'test'}, methods=['GET', 'POST'])
@app.route('/<str1>/<str2>/', methods=['GET', 'POST'])
def landing_page(str1, str2):
    matching_ratio = failureMatcher.matchPercent(str1, str2)
    diff_str1 = str1.split(' ')
    diff_str2 = str2.split(' ')
    html = differ.make_file(diff_str1, diff_str2, context=True)
    return render_template('test.html', str1 = str1, str2 = str2, matching_ratio = matching_ratio, html=Markup(html))

@app.route('/dump/', defaults={'str1':'test', 'str2':'test'}, methods=['GET', 'POST'])
@app.route('/dump/<str1>/<str2>/')
def dumpingData(str1, str2):
    matching_ratio = failureMatcher.matchPercent(str1, str2)
    return {'string1':str1, 'string2':str2, 'matching_ratio':matching_ratio}

@app.route('/curldump/', methods=['POST'])
@app.route('/curldump', methods=['POST'])
def curldump():
    '''
        # curl -i -H "Content-Type: application/json" -X POST -d '{"str1":"aaa/bbb/cg hgfhjf 7635U^%&^% ^*&&*^ ", "str2": "jkhguyg **** lkjlihlih/hiujiu"}' http://localhost:8080/curldump/
    '''

    data = request.json
    str1 = data['str1']
    str2 = data['str2']
    matching_ratio = failureMatcher.matchPercent(str1, str2)
    return {'string1': str1, 'string2': str2, 'matching_ratio': matching_ratio}

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)

