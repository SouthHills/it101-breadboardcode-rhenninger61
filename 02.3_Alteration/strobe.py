from gpiozero import LED as LEDClass, Button
from signal import pause
import time

LED = LEDClass(17)  # define ledPin
BUTTON = Button(18)  # define buttonPin
strobing = False

def loop():
    global LED
    
    while True:
        
        if strobing == True:
            LED.on()
            time.sleep(0.5)
            LED.off()
            time.sleep(0.5)
            print('Strobing LED')

def changeLedState():
    global strobing
    strobing = not strobing

def destroy():
    global LED, BUTTON
    # Release resources
    LED.close()
    BUTTON.close()

if __name__ == "__main__":     # Program entrance
    print ("Program is starting...")
    try:
        # If the button gets pressed, call the function
        # This is an event
        BUTTON.when_pressed = changeLedState
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()