from flask import Flask, request

app = Flask(__name__)

response = "Flask Server running"

@app.route('/')
def check_alive():
    return response

@app.route('/query', methods=['POST'])
def receive_query():
    if request.method == 'POST':
        
        global response
        response = request.json # to show post data on root endpoint
        
        query = request.get_json() # put json data in dict
        decide_quantum_classic(query)
        
    return query, 202


def decide_quantum_classic(query):
    with open("dec.txt", "w") as t:
        t.write(str(query))
    


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5100, debug=True)
    
