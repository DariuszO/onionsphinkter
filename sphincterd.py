#!/usr/bin/env python2

import logging
from time import sleep

from sphincter.serial_connection import SphincterSerialHandler
from sphincter.httpserver import SphincterHTTPServerRunner

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(levelname)8s - %(threadName)s/%(funcName)s - %(message)s',
                        datefmt="%Y-%m-%d %H:%M")
    logging.info("ohai, this is sphincterd")
    s = SphincterSerialHandler(device='/dev/ttyACM0')
    s.connect()
    SphincterHTTPServerRunner.start_thread(('localhost', 1337), s)
    
    
    # sleep until CTRL-C, then quit.
    try:
        while True:
            sleep(1)
    except KeyboardInterrupt:
        s.disconnect()
        logging.info("shutting down sphincterd, kthxbai")
