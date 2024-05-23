import time
from switch import Switch

switch = Switch(21)

def loop():
    while True:
        if switch.get_state(): # if button is pressed
            print ('switch is on >>>')     # print information on terminal
        else : # if button is relessed
            print ('switch is off <<<')
        time.sleep(0.1)

if __name__ == '__main__':     # Program entrance
    print ('Program is starting...')
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        switch.close()