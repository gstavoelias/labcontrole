#foi usado o Google Colab para a geração desses códigos

#instalando bibliotecas necessárias
!pip install plotly
!pip install scipy
!pip install matplotlib
!pip install control

#importando módulos necessários
from numpy import arange
from plotly import graph_objects as go
import numpy as np
import control
import time

#valores coletados pelo sensor ultrassônico
y = [14.9999, 14.54, 13.97, 13.51, 13.2, 12.85, 12.99, 12.85, 12.77, 12.49, 12.37, 12.25, 12.15, 12.13, 12.23, 12.33, 12.3, 12.3, 12.14, 12.16, 12.02, 11.89, 11.79, 11.76, 11.69, 11.81, 11.73, 11.81, 11.66, 11.79, 11.8, 11.65, 11.56, 11.44, 11.41, 11.35, 11.45, 11.36, 11.44, 11.46, 11.52, 11.48, 11.46, 11.47, 11.24, 11.27, 11.14, 11.01,
10.9, 11.05, 10.91, 10.99, 11.06, 11.06, 11.03, 10.87, 10.93, 10.74, 10.78, 10.67, 10.72, 10.56, 10.67, 10.51, 10.57, 10.64, 10.65, 10.61, 10.4, 10.48, 10.29, 10.34,
10.23, 10.33, 10.15, 10.21, 10.09, 10.15, 10.16, 10.21, 10.21, 10.18, 10.13, 10.14, 10.08, 9.85, 9.88, 9.75, 9.83, 9.65, 9.71, 9.55, 9.48, 9.6, 9.8, 9.73, 9.48, 9.55, 9.4, 9.43, 9.25, 9.32, 9.21, 9.31, 9.18, 9.23, 9.23, 9.27, 9.28, 9.45, 9.32, 9.04, 9.04, 8.89, 8.97, 8.99, 8.97, 8.92, 8.9, 8.9, 8.9, 8.88, 8.79, 8.75, 8.52, 8.56, 8.42, 8.51, 8.72, 8.62, 8.54, 8.66, 8.58, 8.68, 8.75, 8.59, 8.62, 8.44, 8.5, 8.39, 8.32, 8.43, 8.49, 8.28, 8.14, 8.05, 7.97, 8.14, 8.22, 8.27, 8.1, 7.97, 8.05, 7.87, 7.77, 7.75, 7.88, 7.93, 7.8, 7.69, 7.6, 7.69, 7.73, 7.58, 7.64, 7.48, 7.59, 7.64, 7.49, 7.55, 7.41, 7.48, 7.32, 7.18, 7.08, 7.01, 6.95, 6.91, 6.86, 6.63, 6.71, 6.92, 6.86, 6.83, 6.78, 6.75, 6.71, 6.65, 6.62, 6.58, 6.56, 6.51, 6.49, 6.45, 6.43, 6.21, 6.23, 6.2, 6.35, 6.25, 6.16, 6.11, 6.25, 6.13, 5.87, 5.88, 5.69, 5.74, 5.78, 5.78,
5.78, 5.75, 5.73, 5.7, 5.66, 5.63, 5.79, 5.68, 5.62, 5.55, 5.49, 5.63, 5.34, 5.36, 5.37, 5.37, 5.37, 5.37, 5.54, 5.46, 5.55, 5.61, 5.45, 5.32, 5.41, 5.3, 5.21, 5.32,
5.37, 5.23, 5.31, 5.17, 5.25, 5.13, 5.03, 5.16, 5.2, 5.06, 4.97, 5.09, 5.16, 5.2, 5.06, 5.01, 4.98, 4.79, 5.02, 4.97, 4.93, 4.91, 4.92, 5.1, 5.01, 4.98, 5.14, 5.23, 5.28, 5.08, 5.15, 5.2, 5.22, 5.07, 5.15, 5.19, 5.24, 5.1, 5.02, 5.14, 5.38, 5.19, 5.04, 4.95, 4.9, 4.87, 4.85, 4.83, 5.02, 4.94, 4.85, 4.79, 4.76, 4.74, 4.77, 4.98, 5.11, 4.99, 4.92, 4.88, 4.86, 4.84, 4.83, 4.82, 4.82, 4.82, 4.82, 4.77, 4.74, 4.73, 4.72, 4.76, 4.78, 4.79, 4.8, 4.81, 4.81, 4.81, 4.81, 4.81, 4.81, 4.81, 4.81, 4.77, 4.75, 4.73, 4.71, 4.71, 4.75, 4.78, 4.79, 4.8, 4.81, 4.81, 4.81, 4.81, 4.81, 4.81, 4.81, 4.81, 4.77, 4.75, 4.73, 4.72, 4.76, 4.78, 4.79, 4.8, 4.81, 4.81, 4.81, 4.81, 4.81, 4.81, 4.81, 4.81, 4.81, 4.77, 4.75, 4.73, 4.72, 4.76, 4.78, 4.79, 4.8, 4.81, 4.81, 4.81, 4.81, 4.81, 4.81, 4.81, 4.81, 4.77, 4.74, 4.73, 4.72, 4.71, 4.75, 4.78,
4.79, 4.8, 4.81, 4.81, 4.81, 4.81, 4.81, 4.81, 4.81, 4.81, 4.77, 4.75, 4.73, 4.72, 4.76, 4.78, 4.79, 4.8, 4.81, 4.81, 4.81, 4.81, 4.81, 4.81, 4.81, 4.81, 4.77, 4.75,
4.72, 4.71, 4.71, 4.75, 4.78, 4.79, 4.8, 4.81, 4.81, 4.81, 4.81, 4.81, 4.81, 4.81, 4.81, 4.77, 4.75, 4.73, 4.72, 4.75, 4.78, 4.79, 4.8, 4.81, 4.81, 4.81, 4.81, 4.81,
4.81, 4.81, 4.81, 4.81, 4.77, 4.75, 4.73, 4.72, 4.76, 4.78, 4.79, 4.8, 4.81, 4.81, 4.81, 4.81, 4.81, 4.81, 4.81, 4.81, 4.8, 4.76, 4.74, 4.72, 4.72, 4.76, 4.78, 4.79,
4.8, 4.81, 4.81, 4.81, 4.81, 4.81, 4.81, 4.81, 4.81, 4.77, 4.75, 4.73, 4.72, 4.76, 4.78, 4.79, 4.8, 4.81, 4.81, 4.81, 4.81, 4.81, 4.81, 4.81, 4.81, 4.81, 4.77, 4.75,
4.73, 4.72, 4.76, 4.78, 4.79, 4.8, 4.81, 4.81, 4.81, 4.81, 4.81, 4.81, 4.81, 4.81, 4.77, 4.75, 4.73, 4.72, 4.76, 4.78, 4.79, 4.8, 4.81, 4.81, 4.81, 4.81, 4.81, 4.81,
4.81, 4.81, 4.77, 4.74, 4.73, 4.72, 4.71, 4.75, 4.78, 4.79, 4.8, 4.81, 4.81, 4.81, 4.81, 4.81, 4.81, 4.81, 4.81, 4.77, 4.75, 4.73, 4.72, 4.76, 4.78, 4.79, 4.8, 4.81,
4.81, 4.81, 4.81, 4.81, 4.81, 4.81, 4.81, 4.77, 4.75, 4.73, 4.72, 4.72, 4.75, 4.78, 4.79, 4.8, 4.81, 4.81, 4.81, 4.81, 4.81, 4.81, 4.81, 4.81, 4.77, 4.75, 4.73, 4.72, 4.76, 4.78, 4.79, 4.8, 4.81, 4.81, 4.81, 4.81, 4.81, 4.81, 4.81, 4.81, 4.81, 4.77, 4.75, 4.73, 4.72, 4.76, 4.78, 4.79, 4.8, 4.81, 4.81, 4.81, 4.81, 4.81]

#vetor do tempo(estimativa de coleta de amostras. Para ser preciso, ainda é necessário utilizar uma função de interrupção para garantir o tempo exato)
x = np.linspace(0.01, 40, 600)

#vetor do complemento da leitura
y2 = []
for i in y:
  valor = 15 - i
  y2.append(valor)

#Função de Transferência teórica
G = control.tf([10.29/(2.93)],[5.45,1])
t,y5 = control.step_response(G,x)

#Representação simples para plotar um degrau, que será plotado no gráfico
deg = []
for i in x:
  degrau = 2.93
  deg.append(degrau)
deg[0] = 0

#Gráfico das Leituras do Sensor
sensor = go.Figure(data=go.Scatter(y=y, x=x, name="Leituras do ultrassônico", ), layout_xaxis_range=[0,40])
sensor.update_layout(
    title="Leituras do Ultrassônico",
    yaxis_title="Altura (cm)",
    xaxis_title="Tempo (seg)",
    legend_title="Legendas",
    font=dict(
        family="Times New Roman",
        size=12,
        color="Black"
    )
)
sensor.show()

#Gráfico do Complemento das Leituras do Sensor
sensor_inv = go.Figure(data=go.Scatter(y=y2, x=x, name="Leituras do ultrassônico realocadas"), layout_xaxis_range=[0,40])
sensor_inv.update_layout(
    title="Leituras do Ultrassônico Realocadas",
    yaxis_title="Altura (cm)",
    xaxis_title="Tempo (seg)",
    legend_title="Legendas",
    font=dict(
        family="Times New Roman",
        size=12,
        color="Black"
    )
)
sensor_inv.show()

#Gráfico para as comparações das curvas
graf_comp = sensor_inv = go.Figure(data=go.Scatter(y=y2, x=x, name="Leituras do ultrassônico realocadas (cm)"), layout_xaxis_range=[0,40])
graf_comp.add_trace(go.Scatter(y=y5*2.93, x=x, name="Curva ajustada (cm)"))
graf_comp.add_trace(go.Scatter(y=deg, x=x, name="Degrau (V)"))
graf_comp.update_layout(
    title="Comparação de Leituras",
    yaxis_title="Amplitude",
    xaxis_title="Tempo (seg)",
    legend_title="Legendas",
    font=dict(
        family="Times New Roman",
        size=12,
        color="Black"
    )
)
graf_comp.show()

#Gráfico do erro Relativo
erro = go.Figure(data=go.Scatter(y=(y2-(y5*2.93))/y2, x=x, name="Erro Relativo"), layout_xaxis_range=[0,40])
erro.update_layout(
    title="Erro Relativo",
    yaxis_title="Magnitude (%)",
    xaxis_title="Tempo (seg)",
    legend_title="Legendas",
    font=dict(
        family="Times New Roman",
        size=12,
        color="Black"
    )
)
erro.show()
