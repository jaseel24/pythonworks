# lst=[10,20,20,30,5,5,6]
# st=set(lst)
# print(st)

st1={12,34,56,788,89,89,9}
st2={6,7,8,4,3,5,6,788,89,7,7,8}
set_union=st2.union(st1)
print(set_union)

intersection_set=st1.intersection(st2)
print(intersection_set)

# differece_st=st1.difference(st2)
# print(differece_st)
#
st1=["ram","ravi","hari","tom"]
passed=["ram","hari"]

failest_std=set(st1).difference(set(passed))
print("failed:",failest_std)
