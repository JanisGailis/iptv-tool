"""
Test the event capture library.
"""

from evdev import InputDevice, categorize, ecodes

device = InputDevice('/dev/input/event0')

for event in device.read_loop():
    if event.type == ecodes.EV_KEY:
        print str(categorize(event))
