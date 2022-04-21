# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 13:33:10 2019

@author: 梁嘉勝

@平時作業2 參考解答
"""


# Homework 2-1

try:
   price = int(input("請輸入商品金額："))   
   if (price>0):       
       print("百元張數為",price//100)
       print("五元個數為",(price%100)//5)
       print("一元個數為",(price%100)%5)
   else:
       print("錯誤：商品必需為正整數!!")   
except ValueError:
   print("錯誤：商品必需為整數型態!!")

# Homework 2-2

try:
   x = int(input("請輸入X軸座標位置：")) 
   y = int(input("請輸入Y軸座標位置：")) 
   loc=""#象限位置
   flag=""#是否在範圍內
   
   if (x>0 and y>0) and (x<=100 and y<=100):
       loc="第一象限"
       flag="Y"
   elif(x<0 and y>0):
       loc="第二象限"
       flag="N"
   elif(x<0 and y<0):
       loc="第三象限"
       flag="N"
   elif(x>0 and y<0):
       loc="第四象限"
       flag="N"
   elif(x==0 and y==0):
       loc="原點"    
       flag="Y"
   elif(x==0 and 0<y<=100):       
       loc="Y軸"    
       flag="Y"       
   elif(y==0 and 0<x<=100):       
       loc="X軸"    
       flag="Y"              
   elif(x==0 and y<0):       
       loc="Y軸"    
       flag="N"       
   elif(y==0 and x<0):       
       loc="X軸"    
       flag="N"                  
   print(loc,flag) 
except ValueError:
   print("錯誤：座標位置需為整數型態!!")




# Homework 2-3



PayType=input("請輸入付費方式:")

if PayType=="線上付款":
    kind=input("請輸入付款種類:")
    if kind=="信用卡付款":
        print("使用信用卡付款")
    elif kind=="網路ATM付款":
        print("使用網路ATM付款")
    elif kind=="LinePay付款":
        print("使用LinePay付款")
    else:
        print("使用悠遊卡付款")
        
else:
    print("使用貨到付款")
    
    



