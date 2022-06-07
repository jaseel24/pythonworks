# expenses=[5679,987,123,657]
# for amount in expenses:
#     print(amount)
# nam=["jab","kjrghdfh","rgdfgghg"]
# print(nam[0])
#even numbers from list
number=[12,13,14,15,-16,-17,-18,0,0]
# for num in number:
#     if num%2==0:
#         print(num)
#sdfvsd
# for num in number:
#     if num>15:
#         print(num+1)
#     if num<15:
#        print(num-1)
#     if num==15:
#         print(num)
#count of even od and zero
# pos_count=0
# neg_count=0
# zero_count=0
# for num in number:
#     if num>0:
#         pos_count+=1
#     if num<0:
#         neg_count+=1
#     if num==0:
#         zero_count+=1
# print(pos_count)
# print(neg_count)
# print(zero_count)
#print from limit from list
# for num in number:
#     if num>=14 and num<=18:
#         print(num)
# number.append(15)
# print(number)
# pos_sum=0
# neg_sum=0
# for num in number:
#     if num>0:
#         pos_sum=pos_sum+num
#     if num<0:
#         neg_sum=neg_sum+num
# print(pos_sum)
# print(neg_sum)
# element=15
# for num in number:
#     if num==element:
#         print("number is in the list")
#         break
# if num!=element:
#     print("number not found")
element=1
flage=0
for i in range(0,len(number)):
    if element==number[i]:
        flage=1
        break
print("number is found"if flage==1 else "num not found")