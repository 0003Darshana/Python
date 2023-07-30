import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(input('Enter the location: '))
v=input('Enter the column name: ')
df[v] = pd.to_datetime(df[v])
df.plot()
plt.show()
