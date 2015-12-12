"""
Handle the events captured by the main module.
"""

from evdev import categorize, ecodes
import json
from iptv import Iptv

class EventHandler(object):
    """
    Handles the captured events.
    """
    def __init__(self):
        # Open settings
        with open("settings.json") as settings_file:
            self.settings = json.load(settings_file)

        self.iptv = Iptv()

    def handle(self, event):
        """
        Do something meaningful with the provided event.
        """
        if not self.filter_event(event):
            return None

        key = ecodes.KEY[event.code][4:]
        
        try:
            # Call a 'set channel number' function
            self.iptv.set_channel(int(key))
            return None
        except ValueError:
            pass

        if key == self.settings["start_tv_key"]:
            self.iptv.switch_on()

        elif key == self.settings["stop_tv_key"]:
            self.iptv.switch_off()

        elif key == self.settings["channel_down"]:
            self.iptv.previous_channel()

        elif key == self.settings["channel_up"]:
            self.iptv.next_channel()

        elif key == self.settings["volume_down"]:
            self.iptv.volume_down()

        elif key == self.settings["volume_up"]:
            self.iptv.volume_up()

    def filter_event(self, event):
        """
        Filter out all unneeded events.
        """

        # Filter out if not a key event.
        if event.type != ecodes.EV_KEY:
            return False

        # Filter out if a key 'down' event.
        if event.value != 0:
            return False

        # Filter out if a key is not found in settings.json
        if ecodes.KEY[event.code][4:] not in self.settings["accepted_keys"]:
            return False

        return True

    def output(self, event):
        """
        Print the event to stdout in a readable format.
        """
        print categorize(event)
