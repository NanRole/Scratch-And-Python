# 4-1-1：
'''
請問在python程式中如何呼叫此函式?
Ans：fnHello()
請問呼叫此函式後，輸出結果為何?
Ans：Hi
'''
# 4-1-2：
def fnHello(name):
    print(f"Hi {name}")
name=input()
fnHello(name)

# 4-2：
import math
def xy(point):
    s=''
    for i in range(2,len(point)-1):
        s+=point[i]
    x,y=s.split(',')
    return eval(x),eval(y)
def distance(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)
A,B=input().split()
x1,y1=xy(A)
x2,y2=xy(B)
print(distance(x1,y1,x2,y2))
