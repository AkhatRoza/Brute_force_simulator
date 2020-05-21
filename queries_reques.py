import requests


def request_local_server(login,password):# Aim of this function = understand the password and login are True or Not
    # on the server
    response = requests.post('http://127.0.0.1:5000/auth',
                             json={'login': login, 'password': password})
    # if response.status_code == 200:
    #     print('Success!')
    #     return True
    # else:
    #     return False
    return response.status_code == 200
# if the server always send 200. We haveto modify that type of code above.

def request_protected_local_server(login,password):# Aim of this function = understand the password and login are True or Not
    # on the server
    response = requests.post('http://127.0.0.1:4000/auth',
                             json={'login': login, 'password': password})
    # if response.status_code == 200:
    #     print('Success!')
    #     return True
    # else:
    #     return False
    return response.status_code == 200
#if the server has engine which resend all to 4000 port not 5000.IF we want to breake a website like Skillbox
#we have to put URL except the http and so on.
#If to breake another resourse we just add here another function def request skillbox.