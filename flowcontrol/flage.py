# num=5
# flag=0
# for i in range(2,num):
#     if num%i==0:
#         flag=1
#         break
# if flag==0:
#     print("prime")
# else:
#     print("not prime")
def flag(num):
    flag = 0
    for i in range(2, num):
        if (num % i == 0):
            flag = 1
            break
    return True if flag==0 else False

def prime_range(n1,n2):
    for num in range(n1,n2+1):
        if flag(num):
            print(num)


prime_range(6,20)

