import numpy as np
import pandas as pd

obj = pd.Series([4,7,-5,3])
print (obj)
print(obj.values)
print(obj.index)
# print(obj.types) 오류 발생
print(obj.dtypes)

obj2 = pd.Series([4,7,-5,3], ['d','b','a','c'])
print(obj2)

# python의 dictionary 자료형을 Series data로 만들 수 있다.
# dictionary의 key가 Series의 index가 된다
data = {'kim': 35000, 'bewoom': 50000, 'joan': 43900}
obj3 = pd.Series(data)
print(obj3)

obj3.name = 'salary'
obj3.index.name = "names"
print(obj3)

'''Data Frame 정의하기
이전에 DataFrame에 들어갈 데이터를 정의해 주어야 하는데,
이는 python의 dictionary 또는 numpy의 array로 정의할 수 있다'''

data = {'name' :['Beomwoo','Cha','Kim','Park']
        ,'year' :[2013, 2014, 2015, 2020]
        , 'points': [1.5, 1.6, 1.4, 2.0]}
df=pd.DataFrame(data)
print(df)
print(df.index)
print(df.columns)
print(df.values) # 값 얻기
# 각 인덱스에 대한 이름 설정하기
df.index.name = 'num'
df.columns.name = 'info'
print(df)
print('\n--------10\n')
# DataFrame을 만들어서 columns와 index를 설정할 수 있다.
df52 = pd.DataFrame(data, columns=['year', 'name', 'points', 'penalty']
                   ,index=['one', 'two', 'three', 'four'])
print(df52)

print('\n--------11\n')

# describe() 함수는 DataFrame의 계산 가능한 값들에 대한 다양한 계산 값을 보여준다.
print(df52.describe())

print('\n--------12\n')
data = {"names": ["Kilho", "Kilho", "Kilho", "Charles", "Charles"],
           "year": [2014, 2015, 2016, 2015, 2016],
           "points": [1.5, 1.7, 3.6, 2.4, 2.9]}
df = pd.DataFrame(data, columns=["year", "names", "points", "penalty"],
                          index=["one", "two", "three", "four", "five"])
print(df)

print('\n--------13\n')
data = {"names": ["Kilho", "Kilho", "Kilho", "Charles", "Charles"],
           "year": [2014, 2015, 2016, 2015, 2016],
           "points": [1.5, 1.7, 3.6, 2.4, 2.9]}
print(data)

print('\n--------14\n')
print(df.year)
print('\n--------15\n')
print(df[['year','points']])
print('\n--------16\n')
df['penalty'] = 0.5
print(df)

print('\n--------17\n')
df['penalty'] = [0.5,0.1,0.4,0.3,0]
print(df)
print('\n--------18\n')
#새로운 열 추가하기
df['zeros'] = np.arange(5)
print(df)
#52번까지 공부. doorbw.tistory.com/172