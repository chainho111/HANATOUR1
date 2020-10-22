from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
import pandas as pd

iris_set = load_iris()
iris_data = iris_set.data
irisDF = pd.DataFrame(data=iris_data, columns=iris_set.feature_names)

print(irisDF.mean())
print(irisDF.var())
#print(irisDF.mean())
sepal length (cm)   5.843333
sepal width (cm)     3.057333
petal length (cm)    3.758000
petal width (cm)     1.199333
dtype: float64

#print(irisDF.var())
sepal length (cm)    0.685694
sepal width (cm)     0.189979
petal length (cm)    3.116278
petal width (cm)     0.581006
dtype: float64

scaler = StandardScaler()
scaler.fit(irisDF)
iris_scaled = scaler.transform(irisDF)

irisDF_scaled = pd.DataFrame(data=iris_scaled, columns=iris_set.feature_names)

print(irisDF_scaled.mean())
print(irisDF_scaled.var())
