import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dir = r"F:\MIS-PDS\CO2Emission"
VehicleData = pd.read_table(dir+r'\VehicleCO2.csv', sep=',')
VehicleData.head()

VehicleData.query("`Vehicel Make`=='BMW' and `Vehicel Model`=='X7'").agg({"CO2 (particles per million)":["mean"]})
VehicleData.query("`Vehicel Make`=='BMW' and `Vehicel Model`=='X5'").agg({"CO2 (particles per million)":["mean"]})
VehicleData.query("`Vehicel Make`=='BMW' and `Vehicel Model`=='X3'").agg({"CO2 (particles per million)":["mean"]})
VehicleData.query("`Vehicel Make`=='BMW' and `Vehicel Model`=='X2'").agg({"CO2 (particles per million)":["mean"]})
VehicleData.query("`Vehicel Make`=='BMW' and `Vehicel Model`=='M8'").agg({"CO2 (particles per million)":["mean"]})
VehicleData.query("`Vehicel Make`=='BMW' and `Vehicel Model`=='M340'").agg({"CO2 (particles per million)":["mean"]})
VehicleData.query("`Vehicel Make`=='BMW' and `Vehicel Model`=='550'").agg({"CO2 (particles per million)":["mean"]})
VehicleData.query("`Vehicel Make`=='BMW' and `Vehicel Model`=='320 i x-drive'").agg({"CO2 (particles per million)":["mean"]})
VehicleData.query("`Vehicel Make`=='BMW' and `Vehicel Model`=='M8 Gran Coupe'").agg({"CO2 (particles per million)":["mean"]})
VehicleData.query("`Vehicel Make`=='BMW' and `Vehicel Model`=='B8 Gran Coupe'").agg({"CO2 (particles per million)":["mean"]})

x = ["217.1","205.8","203.0","198.0","246.0","232.0","232.666667","209.5","235.5","240.0"]
n = 10
r = np.arange(n)
width = 0.25
plt.bar(r, x, color = 'b',width = width, edgecolor = 'black',label='BMW')

VehicleData.query("`Vehicel Make`=='BMW'").agg({"CO2 (particles per million)":["sum"]})

x = [9914,10321,9899,15245]
y = ['BMW','AUDI','BENZ','VW']
n = 4
r = np.arange(n)
width = 0.25
plt.pie(x, labels = y)
plt.show()

