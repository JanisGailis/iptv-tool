"""
Handle the events captured by the main module.
"""

from evdev import categorize, ecodes
import json

class EventHandler(object):
    """
    Handles the captured events.
    """
    def __init__(self):
        # Open settings
        with open("settings.json") as settings_file:
            self.settings = json.load(settings_file)

    def handle(self, event):
        """
        Do something meaningful with the provided event.
        """
        if not self.filter_event(event):
            return None

        key = ecodes.KEY[event.code][4:]
        
        try:
            int(key)
            # Call a 'set channel number' function
            #return None
        except ValueError:
            pass

        # TODO: Read PEP 3103 to figure out how to do this best

        if key == self.settings["start_tv_key"]:
            # Call 'switch on' function
            #return None
            pass

        if key == self.settings["stop_tv_key"]:
            # Call 'switch off' function
            #return None
            pass

        if key == self.settings["channel_down"]:
            # Call 'channel down' function
            # return None
            pass

        if key == self.settings["channel_up"]:
            # Call channel up function
            # return None
            pass

        if key == self.settings["volume_down"]:
            # Call volume up function
            # return None
            pass

        if key == self.settings["volume_up"]:
            # Call volume up function
            # return None
            pass

        self.output(event)

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
