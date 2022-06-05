num=6
for i in range(0,num):#to print rows
    for j in range(1,num-i):#to print space in columse
        print(end=" ")
    for k in range(i+1):#to print star
        print("*",end=" ")
    print()#to go to next line


# for row in range(1,5):
#     for j in range(1,5-row):
#         print(end=" ")
#     for col in range(1,row+1):
#         print("*",end=" ")
#     print()
# for r in range(1,5):
#     for c in range(0,7):
#         if(r==4)or(c+r==4)or(c-r==2):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()