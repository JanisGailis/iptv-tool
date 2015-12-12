"""
Test the event capture library.
"""

from evdev import InputDevice
from event_handler import EventHandler

def main():
    device = InputDevice('/dev/input/event0')
    handler = EventHandler()

    for event in device.read_loop():
        handler.handle(event)


if __name__=="__main__":
    main()
