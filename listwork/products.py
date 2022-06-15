mobiles = [
    [1000, "samsungA52", "4g", "AMOLED", 27000, "samsung", 12],
    [1001, "samsungA52s", "5g", "AMoLED", 32000, "samsung", 20],
    [1002, "redminote10", "4g", "led", 17000, "redmi", 50],
    [1003, "redminote11pro", "5g", "superAMOLED", 20000, "redmi", 70],
    [1004, "samsungA72", "5g", "AMOLED", 27000, "samsung", 1],
    [1005, "samsungA53", "5g", "AMOLED", 27000, "samsung", 34],
    [1006, "samsungm52", "5g", "AMOLED", 27000, "samsung", 7],
    [1007, "samsungm53", "5g", "AMOLED", 27000, "samsung", 89],
    [1008, "samsungA22", "5g", "AMOLED", 27000, "samsung", 0],
    [1009, "iphone13", "5g", "AMOLED", 97000, "apple", 0],
    [1010, "oneplusnordce2", "5g", "AMOLED", 23000, "oneplus", 67]

]
# out_of_stock=[mob for mob in mobiles if mob[-1]==0]
# print(out_of_stock)

# total_stock=[mob[-1] for mob in mobiles]
# print(sum(total_stock))

# range=[mob for mob in mobiles if mob[-3] in range(20000,30000)]
# print(range)

# five_g_phone=[mob[1] for mob in mobiles if mob[2]=="5g"]
# print(five_g_phone)

# samsung=[mob for mob in mobiles if mob[-2]=="samsung"]
# print(samsung)

# costly_mobiles=max([mob[4]for mob in mobiles])
# cost=[mob for mob in mobiles if mob[4]==costly_mobiles]
# print(cost)

# costly_mobile=max(mobiles,key=lambda m:m[4])
# print(costly_mobile)
#
# low_cost=min(mobiles,key=lambda m:m[4])
# print(low_cost)
#
# mo_ten=[mob[4]==27000 for mob in mobiles]
# print("available"if True in mo_ten else "no")
#
# amoled=[mob for mob in mobiles if mob[3]=="AMOLED"]
# print(amoled)

# mobiles.sort(reverse=True,key=lambda m:m[4])
# print(mobiles)

# mobiles.sort(reverse=True,key=lambda m:m[-1])
# print(mobiles)

mob_ten=[mob[4]==27000 for mob in mobiles]
print("available"if True in mob_ten else "not available")






