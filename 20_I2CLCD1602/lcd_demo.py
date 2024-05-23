# Description: Use the LCD display to display data
from lcd_display import LCDDisplayWrapper as LCDDisplay
from time import sleep
from datetime import datetime

lcd = LCDDisplay()
 
def get_cpu_temp():     # get CPU temperature and store it into file "/sys/class/thermal/thermal_zone0/temp"
    tmp = open('/sys/class/thermal/thermal_zone0/temp')
    cpu = tmp.read()
    tmp.close()
    return '{:.2f}'.format( float(cpu)/1000 ) + ' C'
 
def get_time_now():     # get system time
    return datetime.now().strftime('    %H:%M:%S')
    
def loop():
    while(True):
        lcd.clear()     
        lcd.display_message('CPU: ' + get_cpu_temp(), 1)# display CPU temperature
        lcd.display_message(get_time_now(), 2)   # display the time
        sleep(1)
        
def destroy():
    lcd.clear()
    
if __name__ == '__main__':
    print ('Program is starting ... ')
    try:
        loop()
    except KeyboardInterrupt:
        destroy()