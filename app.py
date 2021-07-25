import json
from flask import Flask, render_template, request, jsonify   

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("InputOutput.html")    
    

@app.route("/submitJSON", methods=["POST"])
def processJSON(): 
    jsonStr = request.get_json()
    
    jsonObj = json.loads(jsonStr)
    response = ""
    temp1 = jsonObj['temp1']
    l = temp1.split(",")
    l = set(l)
    response = str(l)
    return response
    
    
if __name__ == "__main__":
    app.run(debug=True)
    
    
