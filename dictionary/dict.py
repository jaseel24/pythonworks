# book={"name":"atomic habit","auther":"jamesclear","price":250,"pages":300}
# print(book["name"])
# print(book["pages"])
#
# book["color"]="white"
# print(book)
#
# print("name" in book)
#
#
# book["ashy"]="bashi"
# print(book)

# print("cash" in book)

# book["pages"]=250
# print(book)

# book["bashy"]="mouse"
# print(book)

account={"acc.no":1000,
         "opening date":
             "12-3-2014",
         "type":"savings",
         "name":"jaseel",
         "balance":10000}
print(account)


# print("acc" in account)
#
# print(account["acc.no"])
#
#
# account["gender"]="male"
# print(account)
#
# print(account["balance"])
#
# account["balance"]+=1000
# print(account)

# print(account.get("type"))

# if "band" in account:
#     account["band"]="4g"
# else:
#     account["band"]="3g"

account["band"]="5g" if "band" in account else "3g"

if account["balance"]>20000:
    account["balance"]-=1000
else:
    account["balance"]-=500

print(account)