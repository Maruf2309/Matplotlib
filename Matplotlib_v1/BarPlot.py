# BarPlot.py
import matplotlib.pyplot as plt

category = ['A', 'B','C', 'D']
values = [5, 7, 8, 9]

plt.bar(category, values, color='green') # x, y
plt.title('Bar Plot')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()