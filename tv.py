#!/usr/local/bin/python

import subprocess
import time

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
	
