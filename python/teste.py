import time
from numpy import arange
from plotly import graph_objects as go
from scipy.optimize import curve_fit
import numpy as np
import random

#CONFIGURA A COMUNICAÇÃO SERIAL

ser = serial.Serial('COM9', 9600)
time.sleep(2)

#LEITURA E ARMAZENAMENTO DOS DADOS 
y = []
for i in range (600): 
    b = ser.readline() #Lê um byte
    string_n = b.decode() #Decodifica
    string = string_n.rstrip() #Remove \n e \r
    flt = float(string) #Transforma string em float
    # print(flt)
    y.append(flt)
    time.sleep(0.1)
ser.close()

x = np.linspace(0.01, 40, 600)

def objective(x, a, b):
  return 2.718281**(((-1/(b*a))*x))/a + 5


popt, _ = curve_fit(objective, x, y)

a,b = popt
print('y = %.5f * x + %.5f' % (a, b))
fig = go.Figure(data=go.Scatter(y=y, x=x, name="luis"), layout_xaxis_range=[0,40])
# fig.show()

x_line = arange(min(x), max(x), 1)
y_line = objective(x_line, a, b)
fig.add_trace(go.Scatter(y=y_line, x=x_line, name="acyr"))
fig.show()
