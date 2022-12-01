# perf.py
#
# Calculates performance...

import time

def calc_perf(function):
    startTime = time.perf_counter()
    function
    print(f'Performance: {(time.perf_counter() - startTime)} sec')
