import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv(input('Enter file location : '))
v=input('Enter column name : ')
df[v]=pd.to_datetime(df[v])
df.plot()
plt.show()
