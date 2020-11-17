import pandas as pd
from sklearn.datasets import load_iris

iris_data = load_iris()
pandas_df = pd.DataFrame(data=iris_data.data, columns=['sepal_length','sepal_width', 'petal_length','petal_width'])
print('\n----1\n', pandas_df)
print('\n----2\n', type(pandas_df))

print('\n----3\n', pandas_df['sepal_width'].value_counts())

year_feature = pandas_df['sepal_width']
print('\n----4\n', year_feature.head())
year_value = pandas_df['sepal_width'].value_counts()
print('\n----5\n', year_value)
print('\n----6\n', pandas_df.columns)
