# Homework 3-1
# 1. 串列 List
# 2.
poetry=["all rivers run into the sea",
		"bad luck often brings good luck",
		"he that promises too much means nothing",
		"no fire without smoke",
		"one is never too old to learn"]
str1=input()
inpoetry=False
for i in range(len(poetry)):
	if(str1==poetry[i]):
		print(str1.title())
		inpoetry=True
if not(inpoetry):
	print(str1)

# Homework 3-2
Item=[50,100,80,120,60,90]
i=0;
money=1000
while True:
	money-=Item[i]
	if(i==len(Item)-1):
		break
	i+=1
print(money)