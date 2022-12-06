'''
 * Keyestudio 42 in 1 Starter Kit for Raspberry Pi Pico
 * lesson 17.2
 * RGB
 * http://www.keyestudio.com
'''
from machine import Pin, PWM
from time import sleep
pwm_r = PWM(Pin(9))
pwm_g = PWM(Pin(10))
pwm_b = PWM(Pin(11))

pwm_r.freq(1000)
pwm_g.freq(1000)
pwm_b.freq(1000)

def light(red, green, blue):
    pwm_r.duty_u16(red)
    pwm_g.duty_u16(green)
    pwm_b.duty_u16(blue)

while 1:
    light(65535, 0, 0)#red
    sleep(1)
    light(65535, 25088, 0)#orange
    sleep(1)
    light(65535, 65535, 0)#yellow
    sleep(1)
    light(0, 65535, 0)#green
    sleep(1)
    light(0, 0, 65535)#blue
    sleep(1)
    light(0, 65535, 65535)#cyan
    sleep(1)
    light(41216, 8448, 61696)#purple
    sleep(1)