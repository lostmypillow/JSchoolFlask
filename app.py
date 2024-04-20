from flask import Flask, request
from flask import jsonify
import requests
import re
from bs4 import BeautifulSoup

app = Flask(__name__)


@app.route('/get_deps/')
def incrementer():
    dep_list = []
    year = request.args.get('year', default=112, type=int)
    sem = request.args.get('sem', default=2, type=int)
    base_url = "https://aps.ntut.edu.tw/course/tw/Subj.jsp?format=-2&year=" + str(year) + "&sem=" + str(sem)
    print(base_url)
    get_deps = BeautifulSoup(requests.get(base_url).content, "html.parser").find_all("a")
    for dep in get_deps:
        dep_list.append(dep.text)
        # print(dep.text)
    return jsonify(
        {
            'deps': dep_list
        }
    )


# @app.before_request
# def before():
#     print("This is executed BEFORE each request.")
#
#
# @app.route('/hello/', methods=['GET', 'POST'])
# def welcome():
#     return "Hello World!"
#
#
# @app.route('/<string:name>/')
# def hello(name):
#     return "Hello " + name
#
#
# @app.route('/person/')
# def person():
#     return jsonify({'name': 'Jimit',
#                     'address': 'India'})
#

if __name__ == '__main__':
    app.run(host='localhost', port=3000)
