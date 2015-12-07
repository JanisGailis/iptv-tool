"""
Test how to create a daemon.
"""

import time, logging
import daemon
from evdev import InputDevice, categorize, ecodes

class Application(object):
    def __init__(self):
        self.keyboard = InputDevice('/dev/input/event0')

    def run(self):
        #while True:
        #    logger.debug("Debug message")
        #    logger.warn("Warning message")
        #    logger.error("Error message")
        #    logger.info("Info message")
        #    time.sleep(10)
        for event in self.keyboard.read_loop():
            logger.info("Parampampam")
            if event.type == ecodes.EV_KEY:
                logger.info(str(categorize(event)))

logger = logging.getLogger("DaemonLog")
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler = logging.FileHandler("/home/janis/Development/daemon.log")
handler.setFormatter(formatter)
logger.addHandler(handler)

context = daemon.DaemonContext()
context.files_preserve = [handler.stream]

app = Application()

with context:
    app.run()
