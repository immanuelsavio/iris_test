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

for i in file(iris):
    row = x.split(',')