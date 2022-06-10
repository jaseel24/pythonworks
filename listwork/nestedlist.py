lst=[
    [10,11],
    [13,45],
    [50,15],
    [60,70]
]
# for sub in lst:
#     for num in sub:
#         if num>16:
#             print(num)
# flatter_lst=[]
# for sub in lst:
#     for num in sub:
#         flatter_lst.append(num)
# print(max(flatter_lst))
flattrn_lst=[num for sub in lst for num in sub]
print(flattrn_lst)
# num_grt=[num for num in flattrn_lst if num>16]
# print(num_grt)
# num_odd=[num for num in flattrn_lst if num%2!=0]
# print(num_odd)

# num_even=sum([num for num in flattrn_lst if num%2==0])
# print(num_even)
