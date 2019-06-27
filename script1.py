import pandas as pd
import numpy as np
import datetime as dt
from matplotlib import

s1 = np.random.random(10)
s2 = pd.date_range(start = dt.datetime(2018, 1, 1), freq = 'm', periods = 10)
print(s1)
print(s2)

df = pd.DataFrame(s1, s2, columns=['abc'])
print(df)


