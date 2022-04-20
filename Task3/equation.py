#!/usr/bin/env python
import sys
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(10, 4, 8)


def f(x):
	prob = 1/(stdDev * np.sqrt(2* np.pi)) * np.exp(-0.5*((x-mean)/stdDev)**2)
	return prob

mean = np.mean(x)
stdDev = np.std(x)

pdf = f(x)

plt.plot(x, pdf, color = 'red')
plt.xlabel('Data')
plt.ylabel('prob')
plt.show()
