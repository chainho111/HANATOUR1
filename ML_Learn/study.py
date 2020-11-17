import pandas as pd
import matplotlib.pyplot as plt

# print("\n-- \n", "")
# CSV 파일로부터 데이터를 읽어들여 데이터프레임을 만든다. 구분자는 '\t'를 사용한다.
df = pd.read_csv(r'C:\Users\hana\Downloads\gapminder.tsv', sep='\t')
print(df.head())

country_df = df['country']
print(type(country_df))
print('------------1\n')
print(country_df.head())
print('------------2\n')
print(country_df.tail())
print('------------3\n')

# 여러 열들을 추출할 수 있다. 이 때는 열의 리스트를 사용한다.
subset = df[['country', 'continent', 'year']]
print(type(subset))
print('------------4\n')
print(subset.head())

print('------------5\n')
# loc --> 인덱스를 기준으로 행 데이터 추출
# 0번째 인덱스의 데이터를 얻는다
print(df.loc[0])

print('------------6\n')
# 모든 행의 2번째 4번째 열과 마지막 열(-1) 데이터를 얻는다
subset = df.iloc[:,[2,4,-1]]
print(subset.head)

print('------------7\n')

# lifeExp 열을 연도별로 그룹화하여 평균 계산하기
print(df.groupby('year')['lifeExp'].mean())

print('------------8\n')
# 1. year를 기준으로 그룹화 한 데이터 프레임을 얻는다
grouped_year_df = df.groupby('year')
# 2. 위에서 그룹화한 데이터의 lifeExp열을 추출한다
grouped_year_df_lifeExp = grouped_year_df['lifeExp']
# 3. mean 함수를 사용하여 평균값을 얻는다
mean_lifeExp_by_year = grouped_year_df_lifeExp.mean()
print(mean_lifeExp_by_year)

print('------------9\n')
# 다중 열 그룹화하여 평균내기
multi_group_vars = df.groupby(['year', 'continent'])[['lifeExp', 'gdpPercap']].mean()
print(multi_group_vars)
print('------------10\n')
# 그룹화한 데이터 개수 세기
print(df.groupby('continent')['country'].nunique())


global_yearly_life_expectancy = df.groupby('year')['lifeExp'].mean()
print(global_yearly_life_expectancy)
global_yearly_life_expectancy.plot()
plt.show()