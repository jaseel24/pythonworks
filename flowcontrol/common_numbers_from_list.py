lst1=[2,3,4,5,6,7]
lst2=[2,4,6,8]
dup_lst=[]
for num in lst1:
    if num in lst2:
        dup_lst.append(num)
print(dup_lst)


