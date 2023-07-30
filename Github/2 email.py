import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(input('Enter the location of csv file: '))
df.plot()
plt.show()
