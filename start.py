from bottle import run, post, request, response, get, route
import time
import thread
import socket
from state import State
from lock import Lock

# DEFINE
DELAY = 2 # in seconds
SERVER_PORT = 7272 # port the server will run on

# VARS
state = State()
lock = Lock(state)

# FUNCTIONS
def getHostIP():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip

def autoClose():
    try:
        start = time.time() # starting time in seconds
        print('starting close cycle')

        while True:
            # try to close the box every 10 seconds
            now = time.time()
            if now > start + 10:
                start = now
                lock.close()
            
            # wait to preform the next check
            time.sleep(DELAY)

    except KeyboardInterrupt:
        lock.end()

#
# ROUTES
#

@route('/', method='GET')
def state_handler():
    print('Route: State')
    return state.toJson()

@route('/toggle', method='POST')
def toggle_handler():
    print('Route: Toggle')
    lock.toggle()
    return state.toJson()

@route('/music/<time>', method='POST')
def music_handler(time):
    print('Route: Music')
    data = time.split('-')
    amount = int(data[0])
    unit = data[1]
    state.addMusic(amount, unit)
    return state.toJson()


@route('/meditate', method='POST')
def meditate_handler():
    print('Route: Meditate')
    state.addMeditationDay()
    return state.toJson()


@route('/drink', method='POST')
def drink_handler():
    print('Route: Drink')
    state.addDrinkDay()
    return state.toJson()


@route('/cheat', method='POST')
def cheat_handler():
    print('Route: Cheat')
    state.addCheatDay()
    return state.toJson()


#
# MAIN LOOP
#

def main():
    # start the close cycle 
    thread.start_new_thread(autoClose, ())

    # start listening for requests
    ip = getHostIP()
    run(host=ip, port=SERVER_PORT)

# start the program
if __name__ == "__main__":
    main()

