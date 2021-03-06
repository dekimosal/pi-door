#!/usr/bin/env python3
import evdev
from evdev import ecodes

#Constants
KEY_PRESSED = 1
KEY_RELEASED = 0

#Variables
pressed = []
btns_num = [
    ecodes.KEY_KP0,
    ecodes.KEY_KP1,
    ecodes.KEY_KP2,
    ecodes.KEY_KP3,
    ecodes.KEY_KP4,
    ecodes.KEY_KP5,
    ecodes.KEY_KP6,
    ecodes.KEY_KP7,
    ecodes.KEY_KP8,
    ecodes.KEY_KP9
    ]
btns_alt = [
    ecodes.KEY_INSERT,
    ecodes.KEY_END,
    ecodes.KEY_DOWN,
    ecodes.KEY_PAGEDOWN,
    ecodes.KEY_LEFT,
    0,
    ecodes.KEY_RIGHT,
    ecodes.KEY_HOME,
    ecodes.KEY_UP,
    ecodes.KEY_PAGEUP
    ]

#OLD: replaced by key from file
#key = [1, 2, 7, 8]

#Get key from file and convert to ecodes
with open('key', 'r') as file:
    key_str = file.readline().strip()
    key = [int(i) for i in list(key_str)]
key_num = [btns_num[i] for i in key]
key_alt = [btns_alt[i] for i in key]

#Startup debug info
devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
for device in devices:
    print(device.fn, device.name, device.phys)

device = evdev.InputDevice('/dev/input/event0')
print(device)

#Actual reading loop
print("Reading input")
for event in device.read_loop():
    if event.type == ecodes.EV_KEY and event.value == KEY_PRESSED:
        #print(evdev.categorize(event))
        if event.code in btns_num + btns_alt:
            #print("Number pressed")
            pressed.append(event.code)
        elif event.code == ecodes.KEY_KPENTER:
            if (pressed == key_num) or (pressed == key_alt):
                print("*** CODE OK, DOOR WILL OPEN ***")
            else:
                print("Wrong code entered")
            pressed.clear()
