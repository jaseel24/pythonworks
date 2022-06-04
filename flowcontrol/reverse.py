num=734
res=""
while(num!=0):
    lastdigit=num%10
    res=res+str(lastdigit)
    num=num//10
print(res)
# for i in range(0,60,2):
#     print(i)
# number=range(10,0,-2)
# for i in number:
#     print(i)
# for i in range(1,10):
#     if i==8:
#         break
#     print(i)