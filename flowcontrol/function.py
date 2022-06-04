# def add_number(n1,n2):
#     return n1+n2
# print(add_number(10,29))
# def substract(n1,n2):
#     return n1-n2
# print(substract(50,25))
# def smart_sub(n1,n2):
#     return n1-n2 if n1>n2 else n2-n1
# print(smart_sub(5,8))
# def validate_gmail(email):
#     return email.endswith("@gmail.com")
# print(validate_gmail("jaseel@gmail"))
# def factorial_number(num):
#     fact=1
#     for i in range(1,num+1):
#         fact=fact*i
#     return (fact)
# print(factorial_number(5))
# def flag(num):
#     flage = 0
#     for i in range(2, num):
#         if (num % i == 0):
#             flage = 1
#             break
#     if (flage == 0):
#         print("prime")
#     else:
#         print("not prime")
# flag(5)



def prime_range(n1,n2):
    flag=0
    for i in range(n1,n2):
        if i%2==0:
            flag=1
            break
        if flag==0:
            print("i")
        else:
            print("no prime number")
prime_range(2,10)







