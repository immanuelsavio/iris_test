#This is a test file for the iris dataset by Dr. R.A. Fisher

import pandas as pd 
import numpy as np 
import csv
import matplotlib.pyplot as plt 

data1=open('IRIS_Dataset/iris.csv','r')
data2=open('IRIS_Dataset/bezdekIris.csv','r')
FormattedData=list(csv.reader(data1))	#changing raw data to an organised list
#print(FormattedData)

NData = []

for EachLength in FormattedData[1:len(FormattedData)]:
	SepalLength = []
	SepalWidth = []
	PetalLength = []
	PetalWidth = []
	SepalLength.append(float(EachLength[EachLength][0]))
	SepalWidth.append(float(EachLength[1]))
	PetalLength.append(float(EachLength[2]))
	PetalWidth.append(float(EachLength[3]))

#for length in SepalLength[0:len(SepalLength)]:
print(SepalLength[1])

