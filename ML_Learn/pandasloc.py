import pandas as pd

pandas_df = pd.read_csv(r'c:\users\hana\downloads\gapminder.tsv', sep='\t')

print('\n-- type(pandas_df)\n', type(pandas_df))
print('\n-- pandas_df.columns\n', pandas_df.columns)
print('\n-- pandas_df.shape\n', pandas_df.shape)
print('\n-- pandas_df.shape1\n', type(pandas_df.shape))

country_df = pandas_df['country']
print('\n-- c_df.country\n', type(country_df))
print('\n-- c_df.head\n', country_df.head())

subset = pandas_df[['country','continent','year','lifeExp','pop']]
print('\n-----subset.type\n', type(subset))
print('\n-----head.type\n', subset.head())
print('\n-----loc[0]\n', pandas_df.loc[0])

number_of_rows = pandas_df.shape[0]
last_row_index = number_of_rows-1
print('\n-----subset.type\n', pandas_df.loc[last_row_index])
print('\n-----pandas_df.tail\n', pandas_df.tail(1))
print('\n-----pandas_df.iloc0\n', pandas_df.iloc[-1])
