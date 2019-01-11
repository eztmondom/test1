import machine
from ssd1306_setup import WIDTH, HEIGHT, setup
from writer import Writer

# Font
import freesans20
import bme280
import time

valt=False

def callback(p):
    global valt
    valt=not valt

p_fel=machine.Pin(12,machine.Pin.IN, machine.Pin.PULL_UP)
p_fel.irq(trigger=machine.Pin.IRQ_RISING, handler=callback)
i2c = machine.I2C(-1, machine.Pin(4), machine.Pin(5))
ssd = setup(False)  # Create a display instance
wri = Writer(ssd, freesans20)
while(1):
        Writer.set_textpos(ssd, 0, 0)  # verbose = False to suppress console output
        strr=bme280.BME280(i2c=i2c).values[0]+'  \n'
        wri.printstring(strr)
        #if 0:
        if valt==False:
            strr=bme280.BME280(i2c=i2c).values[1]+'   \n'
        else:
            altitude=((1-((float(bme280.BME280(i2c=i2c).values[1].split('h')[0])/1013.25)**0.190284))*145366.45)*0.3048
            strr=str(altitude)+'m   \n'
        wri.printstring(strr)
        strr=bme280.BME280(i2c=i2c).values[2]+'  '
        wri.printstring(strr)
        ssd.show()
        time.sleep(0.5)