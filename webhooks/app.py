import re
from flask import Flask, request, render_template, Response
from logging.config import dictConfig
import json
import requests
from jinja2 import Template
import datetime


# helper function to overide output to stdout (flask)
dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://sys.stdout',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    payload = request.json
    js = json.dumps(payload)
    data = json.loads(js)

    print("connection state is: ", data['state'])
    return render_template('index.html', output=data)


@app.route('/webhooks/topic/connections/', methods=['POST', 'GET'])
def connections():
    payload = request.json
    js = json.dumps(payload)
    data = json.loads(js)

    print('\n\n' + "============= CONNECTIONS ============" +'\n')
    print("Connection status: ", data['state'])
    print("Connection ID is ", data['connection_id'])
    return render_template('index.html', output=data)

@app.route('/webhooks/topic/basicmessages/', methods=['POST'])
def basicmessages():
    # serverurl = 'http://127.0.0.1:5003/server-listener'

    payload = request.json
    js = json.dumps(payload)
    data = json.loads(js)
    msg = data['content']
    print("Message: ", msg)

    # forwarderurl = 'http:127.0.0.1:5003/server-listener'.format(data)
    # response = requests.post(forwarderurl, json=data)
    # print(response.json())
    with open("cache.txt", "w") as cache:
        cache.write(msg)
    return render_template('index.html', output=data)


@app.route('/webhooks/topic/issue_credential/', methods=['POST'])
def issuecreds():
    payload = request.json
    js = json.dumps(payload)
    data = json.loads(js)

    print('\n\n' + "============= CREDENTIAL ISSUANCE v1.0 ============" +'\n')
    print("Issuance status: ", data['state'])
    print("Exchange ID: ", data['cred_ex_id'])

    return render_template('index.html', output=data)


@app.route('/webhooks/topic/issue_credential_v2_0/', methods=['POST'])
def issuecredsv2():
    payload = request.json
    js = json.dumps(payload)
    data = json.loads(js)

    print('\n\n' + "============= CREDENTIAL ISSUANCE V2.0 ============" +'\n')
    print("Issuance status: ", data['state'])
    print("Exchange ID: ", data['cred_ex_id'])
    # print("Comments :", data['cred_proposal']['comment'])
    return render_template('index.html', output=data)


@app.route('/webhooks/topic/problem_report/', methods=['POST'])
def issuecredserror():
    payload = request.json
    js = json.dumps(payload)
    data = json.loads(js)

    print('\n\n' + "============= PROBLEM REPORTS ============" +'\n')
    print("Response: ", data)
    return render_template('index.html', output=data)


@app.route('/webhooks/topic/issue_credential_v2_0_indy/', methods=['POST'])
def issuecreds2indy():
    payload = request.json
    js = json.dumps(payload)
    data = json.loads(js)

    print('\n\n' + "============= CREDENTIAL ISSUANCE V2.0 INDY ============" +'\n')
    print("Revocation & Exchange ID: ", data['cred_ex_id'])
    print("\nCredential: ", data)
    return render_template('index.html', output=data)


@app.route('/webhooks/topic/revocation_registry/', methods=['POST'])
def revocationregistry():
    payload = request.json
    js = json.dumps(payload)
    data = json.loads(js)

    print('\n\n' + "============= REVOCATION REGISTRY ============" +'\n')
    print("Credential Def ID: ", data['cred_def_id'])
    return render_template('index.html', output=data)


@app.route('/webhooks/topic/issuer_cred_rev/', methods=['POST'])
def issuercredrev():
    payload = request.json
    js = json.dumps(payload)
    data = json.loads(js)

    print('\n\n' + "============= ISSUER CREDENTIAL REVOCATION ============" +'\n')
    print("Credential status is: ", data['state'])
    return render_template('index.html', output=data)

@app.route('/webhooks/topic/present_proof/', methods=['POST'])
def presentation():
    payload = request.json
    js = json.dumps(payload)
    data = json.loads(js)
    epoch = int(datetime.datetime.now().timestamp())
    dt = datetime.datetime.now()

    if 'verified' not in data:
        print("Verification not found\n")
        print(data)
        print('\n\n' + "============= CREDENTIAL CHECK ============" +'\n')
        print("Role: ", data['role'])
        print("Status: ", data['state'])
        print("Validity: ", 'invalid')
        print("Valid as epoch: " + str(epoch) + '  @ ' + str(dt) + '\n\n')
    else:
        print("Check is valid\n")
        print(data)
        print('\n\n' + "============= CREDENTIAL CHECK ============" +'\n')
        print("Role: ", data['role'])
        print("Status: ", data['state'])
        print("Validity: ", data['verified'])
        print("Valid as epoch: " + str(epoch) + '  @ ' + str(dt) + '\n\n')

    return render_template('index.html', output=data)

    

###Controller###
