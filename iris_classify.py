from sklearn import tree

from sklearn.model_selection import train_test_split
import pandas as pd 

excel_file = 'IRIS_Dataset/iris.csv'
iris = pd.read_csv(excel_file)
y = iris.species
x=iris.drop('species',axis=1)
x_train, x_test, y_train, y_test = train_test_split(x, y,test_size=0.2)
x_train_arr=[]
x_test_arr=[]
y_train_arr=[]
x_test_arr=[]
print(x_test)
for i in iris):
    row = x.split(',')
    x_train_train.append(float(row[0]))
    y_train_train.append(float(j) for j in row[1:3])

print(x_train_arr)