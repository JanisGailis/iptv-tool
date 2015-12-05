#!/usr/local/bin/python

import subprocess
import time

subprocess.Popen(["google-chrome", "-app=http://tv4free.us/tv3.php"])
process_started = False
winid = None
while not process_started:
    try:
        winid = subprocess.check_output(["xdotool","search","--name","TV4FREE"])
        winid = winid[:8]
        process_started = True
    except subprocess.CalledProcessError:
        pass

subprocess.call(["xdotool", "windowfocus", winid, "key", "F11"])
subprocess.call(["xdotool", "mousemove", "--sync", "230", "65"])
	
