# Description : Use ADC module to read the voltage value of potentiometer.
from pathlib import Path
import sys
from gpiozero import PWMLED
import time

HERE = Path(__file__).parent.parent
sys.path.append(str(HERE / 'Common'))
from ADCDevice import * 

USING_GRAVITECH_ADC = False # Only modify this if you are using a Gravitech ADC

LED_17 = PWMLED(17) #17 is the pin
LED_18 = PWMLED(18)
ADC = ADCDevice() # Define an ADCDevice class object

def setup():
    global ADC
    if(ADC.detectI2C(0x48) and USING_GRAVITECH_ADC): 
        ADC = GravitechADC()
    elif(ADC.detectI2C(0x48)): # Detect the pcf8591.
        ADC = PCF8591()
    elif(ADC.detectI2C(0x4b)): # Detect the ads7830
        ADC = ADS7830()
    else:
        print("No correct I2C address found, \n"
            "Please use command 'i2cdetect -y 1' to check the I2C address! \n"
            "Program Exit. \n")
        exit(-1)
        
def loop():
    global LED_17, LED_18
    while True:
        # read the ADC value of channel 0
        value_17 = ADC.analogRead(0)  # Gets a value between 0 and 255
        # Set LED brightness directly with value from ADC
        LED_17.value = value_17 / 255.0  # Value of PWM LED must be between 0 and 1
        # calculate the voltage value
        voltage = value_17 / 255.0 * 3.3  # 3.3 because we are using the 3.3V lead
        print(f'ADC Value: {value_17} \tVoltage: {voltage:.2f}')
        time.sleep(0.03)
        
        # read the ADC value of channel 1
        value_18 = ADC.analogRead(1)  # Gets a value between 0 and 255
        # Set LED brightness directly with value from ADC
        LED_18.value = value_18 / 255.0  # Value of PWM LED must be between 0 and 1
        # calculate the voltage value
        voltage = value_18 / 255.0 * 3.3  # 3.3 because we are using the 3.3V lead
        print(f'ADC Value: {value_18} \tVoltage: {voltage:.2f}')
        time.sleep(0.03)

def destroy():
    global LED_17, LED_18, ADC
    LED_17.close()
    LED_18.close()
    ADC.close()
    
if __name__ == '__main__':   # Program entrance
    print ('Program is starting ... ')
    try:
        setup()
        loop()
    except KeyboardInterrupt: # Press ctrl-c to end the program.
        destroy()
        
