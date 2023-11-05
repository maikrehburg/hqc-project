from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

html = '''
    <!doctype html>
    <head>
    <title>Flask App</title>
    </head>
    <body>
    <h1>Run your code</h1>
    <form method=post enctype=multipart/form-data>
    <textarea name=code rows=60 cols=80 placeholder='enter code here...'>
    </textarea>
    <br>
    <input type=submit value='Run!'>
    </form>
    <a href="/keys"> get keys from DB</a>
    </body>
    '''

@app.route('/', methods=['GET', 'POST'])
def application_entrypoint():
    if request.method == 'POST':
        send_to_decision_service(request.form["code"])
    
    return html


@app.route('/keys', methods=['GET'])
def get_keys():
    pass


def send_to_decision_service(code: str):
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    payload = {
        "problem" : "sort",
        "code": code
    }
    res = requests.post("http://decision-service:5100/query", json=payload, headers=headers)
    with open("res.txt", "w") as r:
        r.write(str(res.status_code))
    return


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
