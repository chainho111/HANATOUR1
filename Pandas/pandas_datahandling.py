import pandas as pd
from sklearn.datasets import load_iris

iris_data = load_iris()
pandas_df = pd.DataFrame(data=iris_data.data, columns=['sepal_length','sepal_width', 'petal_length','petal_width'])
print(pandas_df)