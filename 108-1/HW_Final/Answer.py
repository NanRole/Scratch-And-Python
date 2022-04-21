# 題目一
def head(s,sheet):
    i=3
    hit=False
    s1='20379435'
    s2='47430762'
    s3='36193504'
    while(i<=8):
        if s[-i:]==s1[-i:] or s[-i:]==s2[-i:] or s[-i:]==s3[-i:]: 
            i+=1
            hit=True
        else:
            break
    if hit:
        sheet[11-i]+=1
        
def addSix(s,sheet):
    s1='693'
    s2='043'
    s3='425'
    if s[-3:]==s1 or s[-3:]==s2 or s[-3:]==s3:
        sheet[7]+=1  
        
def whichFile(file):
    sheet=[0,0,0,0,0,0,0,0]
    sum=0
    filepath="C:\\Users\\Hank\\Downloads\\"+file   
    with open(filepath,'r') as f:
        for line in f:
            s=''
            for i in range(8):
                s+=line[i]
            if s=='41482012':
                sheet[0]+=1
            elif s=='58837976':
                sheet[1]+=1
            else:
                head(s,sheet)
                addSix(s,sheet)
    for i in range(8):
        if(sheet[i]>0):
            sum+=sheet[i]*money[i]
            print(prize[i]+'，共中{}張，總額{}元'.format(sheet[i],money[i]*sheet[i]))
    print('統一發票中獎累計總額:',sum)
    
money=[10000000,2000000,200000,40000,10000,4000,1000,200]
prize=['特別獎:獎金一千萬元', '特獎:獎金兩百萬元',
       '頭獎:獎金二十萬元', '二獎:獎金四萬元',
       '三獎:獎金一萬元', '四獎:獎金四千元',
       '五獎:獎金一千元', '六獎:獎金兩百元']    

whichFile("ReceiptLottery1000.txt")
whichFile("ReceiptLottery10000.txt")

# 題目二
sign={'牡羊':1,'金牛':2,'雙子':3,'巨蟹':4,'獅子':5,'處女':6,
      '天平':7,'天蠍':8,'射手':9,'魔羯':10,'水瓶':11,'雙魚':12}
luck={0:'上上',1:'大吉',2:'上吉',3:'中吉',4:'中平',5:'中下',6:'下下'}

Y,M,D=input().split()
Y,M,D=int(Y),int(M),int(D)
name=input()
star=input()

birthScore=(Y+M+D)%3
nameScore=0
for i in range(len(name)):
    nameScore+=ord(name[i])-64
nameScore%=len(name)
starScore=sign[star]

result=(birthScore+nameScore+starScore)%7
print(luck[result])
