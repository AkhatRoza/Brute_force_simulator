import json

from flask import Flask, request, Response

app = Flask(__name__)

stats = {
    'attempts': 0,
    'success': 0,
} #dictionary


@app.route('/') #glabnay str
def hello():
    return f'Hello, user! stats={stats}'


@app.route('/auth', methods=['POST']) # via python
def auth():
    stats['attempts'] += 1

    data = request.json
    login = data['login']
    password = data['password']

    with open('users.json') as users_file:
        users = json.load(users_file)

    # users_file = open('users.json')
    # users = json.load(users_file)
    # users_file.close()

    if login in users and users[login] == password:
        status_code = 200
        stats['success'] += 1
    else:
        status_code = 401

    return Response(status=status_code)


if __name__ == '__main__':
    app.run()
