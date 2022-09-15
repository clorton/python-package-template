from datetime import datetime

from .common import fib

class GaussianEmulator:
    def __init__(self):
        print("Instantiated a gaussian emulator.")
        return

    def __str__(self):
        return f"Gaussian Emulator {fib(datetime.now().second)}"
