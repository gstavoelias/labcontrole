import serial
import time
from plotly import graph_objects as go
import numpy as np

ser = serial.Serial('COM9', 9600)
time.sleep(2)

#PLOTTER SERIAL 
data = []
for i in range (50):
    b = ser.readline()
    string_n = b.decode()
    string = string_n.rstrip()
    flt = float(string)
    # print(flt)
    data.append(flt)
    time.sleep(0.1)
ser.close()

#MONTAGEM DO GRÁFICO

t = np.linspace(0.01, 40000, 1000, endpoint=True)

fig = go.Figure(data=go.Scatter(y=data, x=t), layout_xaxis_range=[0,40000])
fig.show()
