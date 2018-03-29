import BinanceAPI
from apscheduler import schedulers

class TyTrading():
    def __init__(self, option):
        # Get argument parse options
        self.option = option
    
    def run(self):
        print(self.option)

        # run indefinitely
        while (True):
            print('hi')