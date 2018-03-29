# -*- coding: UTF-8 -*-
# @yasinkuyu

import sys
import argparse

sys.path.insert(0, './app')

from TyTrading import TyTrading
      
if __name__ == '__main__':
    
    # Set parser
    parser = argparse.ArgumentParser()
    parser.add_argument('--quantity', type=float, help='Buy/Sell Quantity', default=0)
    parser.add_argument('--symbol', type=str, help='Market Symbol (Ex: XVGBTC - XVGETH)', required=True)

    option = parser.parse_args()
    
    # Get start
    t = TyTrading(option)
    t.run()