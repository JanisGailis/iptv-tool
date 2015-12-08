"""
Test the event capture library.
"""

from evdev import InputDevice, categorize, ecodes
from iptv import iptv

def main():
    device = InputDevice('/dev/input/event0')
    tv = iptv()

    for event in device.read_loop():
        if event.type == ecodes.EV_KEY and event.value == 0:
            print str(categorize(event))
            tv.runTV3()

if __name__=="__main__":
    main()

