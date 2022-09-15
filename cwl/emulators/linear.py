from datetime import datetime

from .common import fib

class LinearEmulator:
    def __init__(self):
        print("Instantiated a linear emulator.")
        return

    def __str__(self):
        return f"Linear Emulator {fib(datetime.now().second)}"
