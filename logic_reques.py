import time
def iterate_by_passwords_then_by_logins(login_generator,password_generator,query):
    password_state = None
    while True:
        password, password_state = password_generator(password_state)
        #password, password_state = password_generator(None)
        #login,login_state = login_generator(None)
        login_state = None
        while True:
            login, login_state = login_generator(login_state)
            print('Try:',login,password)
            time.sleep(1)
            if query(login,password):
                print('Good Job',login,password)
            if login_state is None:
                break
        if password_state is None:
            break





def iterate_by_logins_then_by_limited_passwords(login_generator,password_generator, query):
    limit = 1000
    login_state = None
    while True:
        login, login_state = login_generator(login_state)
        password, password_state = password_generator(None)
        for i in range(limit):
            if query(login, password):
                print('Good Job', login, password)
            password, password_state = password_generator(password_state)
            if password_state is None:
                break
        if login_state is None:
            break