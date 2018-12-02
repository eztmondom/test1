import machine
import time
import ssd1306
import bme280

def callback(p):
    print('gomb',p)

def blink():
    while(1):
        led.value(1)
        time.sleep_ms(1000)
        led.value(0)
        time.sleep_ms(1000)
def oled_demo():
    oled.fill(1)
    oled.show()
    oled.fill(0)
    oled.show()
    oled.text('HELLO',0,0)
    oled.text('WORLD!',0,10)
    oled.show()

def bme280_demo():
    bme = bme280.BME280(i2c=i2c)
    print(bme.values)
    bme.values[0]

def check(num):
    pin = machine.Pin(num, machine.Pin.IN, machine.Pin.PULL_UP)
    while(1):
        print(pin.value())
        time.sleep_ms(300)

#bal 0, jobbra 16(RST+LED+BTN), fel 12, le 13, ok 14.

p_bal=machine.Pin(0,machine.Pin.IN, machine.Pin.PULL_UP)
p_bal.irq(trigger=machine.Pin.IRQ_RISING, handler=callback)
#p_jobbra=machine.Pin(16,machine.Pin.IN)
#p_jobbra.irq(trigger=machine.Pin.IRQ_RISING, handler=callback)
p_fel=machine.Pin(12,machine.Pin.IN, machine.Pin.PULL_UP)
p_fel.irq(trigger=machine.Pin.IRQ_RISING, handler=callback)
p_le=machine.Pin(13,machine.Pin.IN, machine.Pin.PULL_UP)
p_le.irq(trigger=machine.Pin.IRQ_RISING, handler=callback)
p_ok=machine.Pin(14,machine.Pin.IN, machine.Pin.PULL_UP)
p_ok.irq(trigger=machine.Pin.IRQ_RISING, handler=callback)

i2c = machine.I2C(-1, machine.Pin(4), machine.Pin(5))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
led=machine.Pin(16,machine.Pin.OUT) #or reset button
bme = bme280.BME280(i2c=i2c)