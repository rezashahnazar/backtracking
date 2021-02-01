# It is a draft - no specific function here

import numpy as np

week = np.random.rand(7,3)
weekFill = np.zeros((7,3), dtype=str)


persons =['A','B','C','D']

for i in range(0,7):
    for j in range(0,3):
        weekFill[i][j] = persons[round(week[i][j]*3)]

print(weekFill)