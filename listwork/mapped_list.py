lst=[
    [10,11],
    [13,45],
    [50,15],
    [60,70]
]
flattrn_lst=[num for sub in lst for num in sub]
print(flattrn_lst)
mapped_lst=[num+1 if num>25 else num-1 for num in flattrn_lst]
print(mapped_lst)
