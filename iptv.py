#!/usr/local/bin/python

import subprocess
import time
from splinter import Browser
import json

class Iptv(object):
    """
    A class for iptv methods.
    """
    def __init__(self):
        """
        Initialization steps.
        """
        self.browser = None
        self.winid = None

        # Read the settings
        with open("settings.json") as settings_file:
            self.settings = json.load(settings_file)

        # Hide the mouse cursor
        subprocess.Popen(["unclutter", "-idle", "0.01"])

        # Determine display width and height
        output = subprocess.check_output(["xrandr"])
        output = output.splitlines()
        for line in output:
            if '*' in line:
                resolution = line

        resolution = resolution.split()[0]
        self.width, self.height = resolution.split('x')

    def runTV3(self):
        """
        Launch chromium in app mode pointing to TV3
        and switch the player to fullscreen.
        """
        subprocess.Popen(["chromium", "-app=http://tv4free.us/tv3.php"])
        process_started = False
        winid = None
        while not process_started:
            try:
                winid = subprocess.check_output(["xdotool","search","--name","TV4FREE"])
                winid = winid[:8]
                process_started = True
            except subprocess.CalledProcessError:
                pass

        output = subprocess.check_output(["xrandr"])
        output = output.splitlines()
        for line in output:
            if '*' in line:
                resolution = line

        resolution = resolution.split()[0]
        width, height = resolution.split('x')

        subprocess.call(["xdotool", "windowfocus", winid, "key", "F11"])
        subprocess.call(["xdotool", "mousemove", "--sync", str(int(width)/2), "150"])
        time.sleep(1)
        subprocess.call(["xdotool", "click", "--repeat", "2", "1"])

    def set_channel(self, channel_nr):
        """
        Set the TV channel to the one denoted by channel_nr
        channel_nr -- an integer denoting the channel
        """
        # Humans count channels starting with one, Python list starting with
        # zero.
        try:
            self.set_url(self.settings["channel_list"][channel_nr-1])
        except IndexError:
            # Requesting a channel outside of the channel list
            pass
                
    def set_url(self, url):
        """
        Set the URL for the current browser session.

        URL -- a string to load in the browser.
        """
        if not self.browser:
            return None

        self.browser.visit(str(url))
        time.sleep(0.5)
        # Maximize the player
        subprocess.call(["xdotool", "click", "--repeat", "2", "1"])

    def next_channel(self):
        """
        Set the next channel in the channel list.
        """
        print "Next channel"

    def previous_channel(self):
        """
        Set the previous channel in the channel list.
        """
        print "Previous channel"

    def switch_on(self):
        """
        Switch the TV application on. That is, open the browser in fullscreen
        mode without any URLs set and hide the mousen.
        """
        # Return if the browser is already open
        if self.browser:
            return None

        self.browser = Browser()
        self.winid = subprocess.check_output(["xdotool","search","--onlyvisible","--all","--name","Iceweasel"])
        self.winid = self.winid[:8]

        subprocess.call(["xdotool", "windowfocus", self.winid, "key", "F11"])
        subprocess.call(["xdotool", "windowfocus", self.winid, "key", "Escape"])
        subprocess.call(["xdotool", "mousemove", "--sync",
            str(int(self.width)/2), str(int(self.height)/4)])

    def switch_off(self):
        """
        Switch the TV application off.
        E.g., kill the browser, don't stop the iptv background process.
        """
        if self.browser:
            self.browser.windows.current.close()
            self.browser = None

    def volume_up(self):
        """
        Increase the system volume.
        """
        print "Volume up."

    def volume_down(self):
        """
        Decrease the system volume.
        """
        print "Volume down."
