g = lambda x:x**2
print(g(8))

print('-'*80)
f = lambda x,y:x+y
print(f(2,2))

print('-'*80)

# inc 함수로 lambda 함수를 즉석에서 생성하고 반환하는 함수를 정의합니다.
# 리턴된 함수는 인수를 작성시 지정된 값만큼 증가시킵니다
def inc(n):
    return lambda x:x+n

f = inc(2)
g = inc(4)
print(f(12))
print(g(12))
print(inc(2)(12))

print('-'*80)

a = [1,2,3,4]
b = [17,12,11,10]
print(list(map(lambda x, y:x+y, a,b)))

print('-'*80)

foo = [2,18,9,22,17,24,8,12,27]
print(list(filter(lambda x:x%3==0,foo)))

print('-'*80)

from functools import reduce
t = [47,11,42,13]
result = reduce(lambda x,y:x+y,t)
print(result)


print('-'*80)

# lambda응용

a = [1,6,2,5,2,7,2,8,9,11,5,26]
result = list(map(lambda x : x**2,a))
print(result)
print('-'*80)
# map을 사용하여 리스트 a에서 2의 배수를 문자열로 반환합니다.
# map은 리스트의 요소를 각각 처리하므로 lambda의 반환값도 요소라야 합니다. 여기서는 요소가 2의 배수일때는 str(x)로 요소를
# 문자열로 만들어서 반환했고, 2의 배수가 아닐때는 x로 요소를 그대로 반환했습니다.
result2 = list(map(lambda x:str(x)if x % 2 == 0 else x, a))
print(result2)

print('-'*80)

b = [12,16,24,5,20,27,12,8,9,110,51,26]
result3 = list(map(lambda x,y:x+y,a,b))
print(result3)

print('-'*80)

a = [8,4,2,5,2,7,9,11,26,13]
result = list(filter(lambda x : x>7 and x < 15, a))
print(result)

print('-----------------1\n')
#python Loop안에 있는 Lambda 식
def square(x):
    return lambda :x * x
listdflambdas  = [square(i) for i in [1,2,3,4,5]]
for f in listdflambdas:
    print(f())

print('-----------------2\n')

listoflambdas = [lambda i=i: i*i for i in range(1,6)]
for f in listdflambdas:
    print(f())