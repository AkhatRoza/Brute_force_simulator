simple_logins = ['admin','jack','cat','jim']


def generate_simple_login(state):
    if state is None:
        state = 0
    if state == len(simple_logins)-1:
        next_state = None
    else:
        next_state = state + 1
    #state-condition which show present condition of generator
    #for logic it should be object that knows nothing about the object
    #just put inside logic and wating that returns according the conditions password or login
    return simple_logins[state],next_state
# we got state and we also retirn next state

with open('10-million-password-list-top-1000000.txt') as f:
    popular_passwords = f.read().split('\n')



def generate_popular_passwords(state):
    if state is None:
        state = 0

    if state == len(popular_passwords)-1:
        next_state = None
    else:
        next_state = state + 1
    #Aim during the new call , the function should give next password
    return popular_passwords[state],next_state
    #fun shows when to generate and shows step


alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'
base = len(alphabet)
def generate_brut_force(state):
    if state is None:
        state = [0,0]

    i,length=state
    password = ''
    temp = i
    while temp != 0:
        rest = temp % base
        temp = temp // base
        password = alphabet[rest] + password

    # while len(password) < length:
    #     password = '0' + password
    password = alphabet[0] * (length - len(password)) + password

    if password == alphabet[-1] * length:
        length += 1
        i = 0
    else:
        i += 1

    next_state = [i , length]

    return password,next_state
    # we waiting that we get new resquest for the generation