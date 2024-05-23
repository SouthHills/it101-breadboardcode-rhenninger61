import RPi.GPIO as GPIO

class Switch():
    switch_pin: int

    def __init__(self, switch_pin, skip_GPIO_setup = False):
        self.switch_pin = switch_pin
        if skip_GPIO_setup == False:
            GPIO.setmode(GPIO.BCM) # use GPIO/BCM numbering
        GPIO.setup(switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # set switchPin to PULL UP INPUT mode
           
    def get_state(self) -> bool:
        return True if GPIO.input(self.switch_pin)==GPIO.LOW else False
           
    def close(self):
        self.__del__()

    def __del__(self):
        GPIO.cleanup()                    # Release GPIO resource