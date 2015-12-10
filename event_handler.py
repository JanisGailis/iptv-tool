"""
Handle the events captured by the main module.
"""

from evdev import categorize, ecodes

class EventHandler(object):
    """
    Handles the captured events.
    """
    def __init__(self):
        pass

    def handle(self, event):
        """
        Do something meaningful with the provided event.
        """
        if not self.filter_event(event):
            return None

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

        return True

    def output(self, event):
        """
        Print the event to stdout in a readable format.
        """
        print categorize(event)
