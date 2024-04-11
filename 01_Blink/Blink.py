from gpiozero import LED as LEDClass # Alias
import time

LED_17 = LEDClass(17)  # define led
LED_18 = LEDClass(18)
def loop():
    global LED_17
    global LED_18
    while True:
        LED_17.on() 
        LED_18.off()
        print ("led 17 turned on, led 18 turned off >>>") # print information on terminal
        time.sleep(1)
        LED_17.off()
        LED_18.on()
        print ("led 17 turned off, led 18 turned on <<<")
        time.sleep(1)
        
def destroy():
    global LED_17, LED_18
    # Release resources
    LED_17.close()
    LED_18.close()

if __name__ == "__main__":    # Program start point
    print("Program is starting ... \n")
    print(f"Using pin {LED_17.pin} and {LED_18.pin}")
    try:
        loop()
    except KeyboardInterrupt:   # Press ctrl-c to end the program.
        destroy()
