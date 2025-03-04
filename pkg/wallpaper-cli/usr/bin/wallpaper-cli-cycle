#!/usr/bin/env python3
from image_manager import ImageManager;
import time;

if __name__ == "__main__":
    # while an instance of this is running
    # load the cycle term every time
    manager = ImageManager();
    if manager.cycle_enable:
        while True:
            # only cycle if its true
            if manager.cycle:
                manager.next_image();
                manager.load_image_pool();
                time.sleep(20);
