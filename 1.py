import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("StudentsPerformance.csv")

plt.ylabel("средняя оценка")
plt.xlabel("тип ланча")
first = df.groupby("lunch")["math score"].mean()

plt.plot(first)
plt.show()

plt.ylabel("макс. оценка по письму")
plt.xlabel("группа")
first = df.groupby("race/ethnicity")["writing score"].max()

plt.plot(first)
plt.show()
