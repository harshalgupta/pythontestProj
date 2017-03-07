import os
from flask import Flask
from flask import request

app = Flask(__name__)

param = None

@app.route("/")
def hello():
    return "The value of your boolean is " + str(param) 

@app.route("/setvalue")
def setvalue():
    global param
    userVal = request.args.get('value')
    if (userVal=='True' or userVal=='true' or userVal=='1'):
        param = True
    elif (userVal=='False' or userVal=='false' or userVal=='0'):
	param = False
    else:
        return "please provide a valid value: True or true or 1 for setting \'True\' or False or false or 0 for setting False"
    
    return "The value of your boolean is " + str(param)	
	
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
