lst=[2,4,6,8]
element=10
# for i in range(0,len(lst)):
#     for j in range((i+1),len(lst)):
#         cur_sum=lst[i]+lst[j]
#         if cur_sum==sum:
#             print(f"pairs{lst[i]},{lst[j]}")
#             break
low=0
upp=len(lst)-1
while low<upp:
    cur_sum=lst[low]+lst[upp]
    if cur_sum==element:
        print(f"pair{lst[low]},{lst[upp]}")
        break
    elif cur_sum>element:
        upp-=1
    elif cur_sum<element:
        low+=1

