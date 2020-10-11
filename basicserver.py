from flask import Flask, request, redirect, session, url_for, Response, json, render_template, send_from_directory
from werkzeug.utils import secure_filename
from flask.json import jsonify
import json
import os
import random
import time
import requests
from requests.structures import CaseInsensitiveDict
from pymongo import MongoClient
from pprint import pprint
from google.cloud import datastore
from google.cloud import vision
from google.cloud import storage
from flask_cors import CORS
import pyttsx3


from bson import ObjectId

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


status = "off"



with open('credentials.json', 'r') as f:
    creds = json.load(f)

mongostr = creds["mongostr"]
client = MongoClient(mongostr)
# response = model.predict_by_url('@@sampleTrain')



db = client["uvbox"]


eng = pyttsx3.init()


def sendSms(dest,message):
    url = "https://api.zang.io/v2/Accounts/ACf674eb3200c199315f0a44c0b9e990ed/SMS/Messages.json"

    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/x-www-form-urlencoded"
    headers["Authorization"] = "Basic QUNmNjc0ZWIzMjAwYzE5OTMxNWYwYTQ0YzBiOWU5OTBlZDpjOTViNDdlZTU1NzQ0NzJkYWFjOTJkNzExNmNjMmJlZQ=="

    data = "From=+19179001701&To="+dest + "&Body=" + message


    resp = requests.post(url, headers=headers, data=data)

    print(resp.status_code)





def getincomingmessage():
    global status

    url = "https://api.zang.io/v2/Accounts/ACf674eb3200c199315f0a44c0b9e990ed/SMS/Messages.json"

    payload = ""
    headers = {
        'Authorization': "Basic QUNmNjc0ZWIzMjAwYzE5OTMxNWYwYTQ0YzBiOWU5OTBlZDpjOTViNDdlZTU1NzQ0NzJkYWFjOTJkNzExNmNjMmJlZQ==",
        'cache-control': "no-cache",
        'Postman-Token': "9c192197-7025-4c32-822c-44cde96c60c0"
        }

    response = requests.request("GET", url, data=payload, headers=headers)

    print(response.text)

    resj = json.loads(response.text)

    incomingText = resj['sms_messages'][0]['body']
    incomingNumber = resj['sms_messages'][0]['from']

    incomingText = incomingText.lower()
    resp = "sorry, i didnt get that. available command are turn sanitron on , turn sanitron off and get sanitron status"

    if "turn sanitron on" in incomingText:
        os.system("sudo python sanitroncontrols.py on")
        eng = pyttsx3.init()
        eng.say("Sanitron turned on.")
        eng.runAndWait()
        status = "on"
        resp = "request acknowledged. sanitron activated"

    if "turn sanitron off" in incomingText:
        os.system("sudo python sanitroncontrols.py off")
        eng = pyttsx3.init()
        eng.say("Sanitron turned off.")
        eng.runAndWait()
        status = "off"
        resp = "request acknowledged. sanitron deactivated"
    
    if "get sanitron status" in incomingText:
        os.system("sudo python sanitroncontrols.py off")
        eng = pyttsx3.init()
        eng.say("sanitron status is " + status)
        # eng.runAndWait()
        resp = "request acknowledged. sanitron is currently " + status

    

    
    print (incomingText)

    sendSms(incomingNumber, resp)





def downloadpic(pic_url):
    

    with open('pic1.jpg', 'wb') as handle:
            response = requests.get(pic_url, stream=True)

            if not response.ok:
                print (response)

            for block in response.iter_content(1024):
                if not block:
                    break


                handle.write(block)


app = Flask(__name__)
app.config.from_object(__name__)
CORS(app)


@app.route("/dummyJson", methods=['GET', 'POST'])
def dummyJson():

    print(request)

    res = request.get_json()
    print (res)

    resraw = request.get_data()
    print (resraw)

##    args = request.args
##    form = request.form
##    values = request.values

##    print (args)
##    print (form)
##    print (values)

##    sres = request.form.to_dict()
 

    status = {}
    status["server"] = "up"
    status["message"] = "some random message here"
    status["request"] = res 

    statusjson = json.dumps(status)

    print(statusjson)

    js = "<html> <body>OK THIS WoRKS</body></html>"

    resp = Response(statusjson, status=200, mimetype='application/json')
    ##resp.headers['Link'] = 'http://google.com'

    return resp


@app.route("/handleIncomingSms", methods=['GET', 'POST'])
def hincomingsms():

    print(request)

    res = request.get_json()
    print (res)

    resraw = request.get_data()
    print (resraw)

##    args = request.args
##    form = request.form
##    values = request.values

##    print (args)
##    print (form)
##    print (values)

##    sres = request.form.to_dict()
 
    getincomingmessage()

    status = {}
    status["server"] = "up"
    status["message"] = "some random message here"
    status["request"] = res 

    statusjson = json.dumps(status)

    print(statusjson)

    js = "<html> <body>OK THIS WoRKS</body></html>"

    resp = Response(statusjson, status=200, mimetype='application/json')
    ##resp.headers['Link'] = 'http://google.com'

    return resp


@app.route("/falldetect", methods=['GET', 'POST'])
def falldetect():

    ##res = request.json

    js = "<html> <body>OK THIS WoRKS</body></html>"
    eng = pyttsx3.init()
    eng.say("Failure detected. Please cancel the alert using your app in the next 60 seconds. If the alert is not cancelled emergency services will be notified.")
    # eng.runAndWait()
    print ("failure detected")
    



    resp = Response(js, status=200, mimetype='text/html')
    ##resp.headers['Link'] = 'http://google.com'

    return resp





@app.route("/dummy", methods=['GET', 'POST'])
def dummy():

    ##res = request.json

    js = "<html> <body>OK THIS WoRKS</body></html>"

    resp = Response(js, status=200, mimetype='text/html')
    ##resp.headers['Link'] = 'http://google.com'

    return resp

@app.route("/api", methods=["GET"])
def index():
    if request.method == "GET":
        return {"hello": "world"}
    else:
        return {"error": 400}


if __name__ == "__main__":
    app.run(debug=True, host = 'localhost', port = 8003)
    # app.run(debug=True, host = '45.79.199.42', port = 8002)
