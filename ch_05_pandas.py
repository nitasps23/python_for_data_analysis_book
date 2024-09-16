import numpy as np
import pandas as pd

price = pd.read_pickle('yahoo_price.pkl')
volumn = pd.read_pickle('yahoo_volumn.pkl')

# returns = price.pct_change()

# returns.tail()