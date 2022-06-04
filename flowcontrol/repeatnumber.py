# num=int(input('Enter number'))
# temp=num
# i=1
# sum=0
# while(i<=num):
#     sum=sum+temp
#     temp=(temp*10)+num
#     i+=1
#
# print(sum)
# num1=15
# num2=35
# hcf=1
# limit=min(num1,num2)
# for i in range(2,(num1+1)):
#     if (num1%i==0)and(num2%i==0):
#         hcf=(i)
#
#
# print(hcf)
# for row in range(1,5):
#     for col in range(1,5):
#         print(row,end=" ")
#     print()
for row in range(1,5):
    for col in range(1,row+1):
        print("*",end=" ")
    print()
