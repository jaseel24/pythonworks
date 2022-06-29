# def min_num(*args):
#     return min(args)
#
# def max_num(*gs):
#     return max(gs)
#
# def add_num(*add):
#     return sum(add)
#
#
#
# print(add_num(10,220,40,50))

def details(**atg):
    print(atg)

details(name="jaseel",place="mkb",age=34)


def add(**add):
    print(sum(v for v in add.values()))

add(a1=10,a2=20,a3=60)

