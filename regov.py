import requests
import json
import os
import time

# from .webhooks.app import basicmessages

conn_id = None


def createinvitation():
    url = 'http://0.0.0.0:3009/connections/create-invitation'

    response = requests.post(url, json={})
    data = response.json()
    global conn_id
    conn_id = data['connection_id']
    return data

def messages(msg):
    # init url / http connection
    url = 'http://0.0.0.0:3009/connections/{}/send-message'.format(conn_id)
    print(url)

    # send message
    dict1 = {'content': msg}
    json_str = json.dumps(dict1)

    response = requests.post(url, json=dict1)
    print(response.json())
    r = response.json()
    return r

def postschema():
    schema = {
    "attributes": [
        "name",
        "phone",
        "ID"
    ],
    "schema_name": "my-license",
    "schema_version": "1.0"
    }

    url = 'http://0.0.0.0:3009/schemas'

    response = requests.post(url, json=schema)
    data = response.json()
    pretty = data['schema']
    print(json.dumps(pretty, indent=4, sort_keys=True))
    input('\n\nPost successful, press any key to continue...')

def postCredDefId():
    cred_def={
    "revocation_registry_size": "100",
    "schema_id": "2uiaGAtZFzCL15n7CcxEYY:2:my-license:1.0",
    "support_revocation": "true",
    "tag": "default"
    }

    url = 'http://0.0.0.0:3009/credential-definitions'

    
    response = requests.post(url, json=cred_def)
    data = cred_def
    print(json.dumps(data, indent=1, sort_keys=True))
    input('\n\nPost successful, refer webhook for ID.\n press any key to continue...')

def accept_proposal():
    pass

def switch():
    os.system("clear")
    print("Welcome to Regov Self-Sovereign Identity (Issuer)\n\n")
    print("                           /#      .*****************.                          ")
    print("                         %%%%%%.      *****,      ,*****                        ")
    print(
        "                      /%%%%%#%%%%(      .*****       *****.                     ")
    print("                    %%%%%/    ,%%%%%       *****,      ******                   ")
    print(
        "                 /%%%%#      *%%%%%%%%(      .*****      .*****.                ")
    print(
        "               %%%%%/      %%%%%(  ,%%%%%.      *****,      ******              ")
    print(
        "            /%%%%%      *%%%%%.       #%%%%(      .*****      .*****.           ")
    print("         .%%%%%/      #%%%%/      .     ,%%%%%.      *****,      ,****,         ")
    print("       /%%%%%      *%%%%%      .*****      #%%%      .*****      .*****         ")
    print(
        "         #%%%%(      (%%%%#       *****.           *****,      ******           ")
    print("           *%%%%%.     .%%%%%,      ,*****      .*****      .*****.             ")
    print(
        "              #%%%%(      (%%%%#       *****. *****,      *****,                ")
    print("                ,%%%%%.     .%%%%%,      ,*******      .*****.                  ")
    print(
        "                   #%%%%#      (%%%%%       *****.   *****,                     ")
    print("                     ,%%%%%.     .%%%%%,      ,*********                        ")
    print(
        "                        #%%%%#((((((%%%%%#       ****,                          ")
    print("                          ,%%%%%%%%%%%%%%%%%.                                   ")
    menu = int(
        input("\nPlease select operation\n\n 1. Create invitation\n 2. Chatroom\n 3. Create Schema\n 4. Post & Get Definition ID \n 5. Send offer \n\nSelection: "))
    os.system("clear")
    # Calling Menu No. 1 Create Invitation
    if menu == 1:
        os.system("clear")
        a = createinvitation()
        b = json.dumps(a['invitation'])
        print("Copy and paste the following invitation below into agent:\n\n", b)
        input("\npress any key to continue...")
        switch()
    elif menu == 2:
        os.system("./chat.sh")
        os.system("clear")
        # messages()
        user_msg = ''
        while user_msg != "bye":
            os.system("clear")
            user_msg = input('Enter message:')
            a = messages(user_msg)
            if user_msg == "bye":
                break
        switch()
    elif menu == 3:
        postschema()
        switch()

    elif menu ==4:
        postCredDefId()
        switch()

    elif menu ==5:
        pass

    else:
        print("Invalid selection. Please try again.")
        time.sleep(1)
        switch()

switch()
