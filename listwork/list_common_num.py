arr1=[1,2,3,4,5,6]
arr2=[2,4,6,7,8,9]
p1=0
p2=0
while(p1<len(arr1)and p2<len(arr2)):
    if arr1[p1]==arr2[p2]:
        print(f"common{arr1[p1]}")
        p1+=1
        p2+=1
    elif arr1[p1]>arr2[p2]:
        p2+=1
    elif arr1[p1]<arr2[p2]:
        p1+=1
