import numpy as np
import pandas as pd

sr = pd.Series([6, 4, 6, 3, 1, 5])

print(sr[sr%3==0])