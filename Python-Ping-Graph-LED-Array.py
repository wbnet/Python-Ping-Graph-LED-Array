#!/usr/bin/env python

# Using Raspberry Pi and Scroll pHAT HD to graph ping times.
# Adjust MAX_VALUE to typical max ping time (ms).

import time
# import random
import os
import re
import scrollphathd

print("""
Scroll pHAT HD: Graph

Displays a graph of ping times.

Press Ctrl+C to exit!

""")

MIN_VALUE = 0
MAX_VALUE = 20

# Uncomment the below if your display is upside down
#   (e.g. if you're using it in a Pimoroni Scroll Bot)
# scrollphathd.rotate(degrees=180)

# Begin with a list of 17 zeros
values = [0] * scrollphathd.DISPLAY_WIDTH

while True:
    # Insert a random value at the beginning
    # values.insert(0, random.randrange(MIN_VALUE, MAX_VALUE))

    hostname = "192.168.50.1"
    # hostname = "www.google.com"
    response = os.popen("ping -c 1 " + hostname + " | tail -n 1").read()

    # print(response)

    x = re.split("\/", response)
    print(x)

    y = x[4]
    print(y)

    z = float(y)
    print(z)

    # values.insert(0, random.randrange(MIN_VALUE, MAX_VALUE))
    values.insert(0, z)

    # Get rid of the last value, keeping the list at 17 (DISPLAY_WIDTH) items
    values = values[:scrollphathd.DISPLAY_WIDTH]

    # Plot the random values onto Scroll pHAT HD
    scrollphathd.set_graph(values, low=MIN_VALUE, high=MAX_VALUE, brightness=0.3)

    scrollphathd.show()
    time.sleep(2.0)
