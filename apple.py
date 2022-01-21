import requests
import json
import os
import time

conn_id = None


def receiveinvitation():
    url = 'http://0.0.0.0:4009/connections/receive-invitation'
    a = input('Enter invitation details: ')
    b = json.loads(a)

    response = requests.post(url, json=b)
    data = response.json()
    global conn_id
    conn_id = data['connection_id']
    return data


def messages(msg):
    # init url / http connection
    url = 'http://0.0.0.0:4009/connections/{}/send-message'.format(conn_id)
    # send message
    dict1 = {'content': msg}
    json_str = json.dumps(dict1)

    response = requests.post(url, json=dict1)
    empty = response.json()
    return None


def switch():
    os.system("clear")
    print("Welcome to Apple Inc. Self-Sovereign Identity (Holder)\n\n")
    print("                                            @@                                 ")
    print(
        "                                         (@@@@@                                ")
    print("                                        @@@@@                                  ")
    print("                                        @&                                     ")
    print("                             @@@@@@@@@@@@@@@@@@@@@@@                           ")
    print("                           @@@@@@@@@@@@@@@@@@@@@@@@@%                          ")
    print("                          @@@@@@@@@@@@@@@@@@@@@@@@&                            ")
    print("                         @@@@@@@@@@@@@@@@@@@@@@@@@                             ")
    print("                         @@@@@@@@@@@@@@@@@@@@@@@@@                             ")
    print("                          @@@@@@@@@@@@@@@@@@@@@@@@@                            ")
    print("                          @@@@@@@@@@@@@@@@@@@@@@@@@@@                          ")
    print("                           @@@@@@@@@@@@@@@@@@@@@@@@@@@                         ")
    print("                            .@@@@@@@@@@@@@@@@@@@@@@@@                          ")
    print("                              @@@@@@@@@@@@@@@@@@@@@                            ")
    print("                                 @@@'#'       .@@ @                            \n\n\n")

    menu = int(
        input("Please select operation\n\n 1. Receive invitation\n 2. Chatroom \n 3. Send message \n 4. View Credential \n 5. Credential status \n\nSelection: "))
    os.system("clear")
    # Calling Menu No. 1 Receive Invitation
    if menu == 1:
        os.system("clear")
        receiveinvitation()
        os.system("clear")
        print("\nSuccessful. Redirecting to main menu...")
        time.sleep(1.5)
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


switch()
