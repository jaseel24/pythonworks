accounts = [
    {
        "acno": 1000, "ac_type": "savings", "balance": 5000, "transactions": [
        {"to": 1001, "amount": 500, "note": "ebill", "method": "g-pay"},
        {"to": 1002, "amount": 600, "note": "geto", "method": "neft"},
        {"to": 1003, "amount": 100, "note": "erchrge", "method": "phone-pay"}
    ]
    },
    {
        "acno": 1001, "ac_type": "savings", "balance": 6000, "transactions": [
        {"to": 1000, "amount": 500, "note": "ebill", "method": "g-pay"},
        {"to": 1002, "amount": 600, "note": "geto", "method": "neft"},
        {"to": 1003, "amount": 100, "note": "erchrge", "method": "phone-pay"}
    ]
    },
    {
        "acno": 1002, "ac_type": "current", "balance": 8000, "transactions": [
        {"to": 1001, "amount": 700, "note": "ebill", "method": "g-pay"},
        {"to": 1000, "amount": 600, "note": "geto", "method": "neft"},
        {"to": 1003, "amount": 800, "note": "erchrge", "method": "phone-pay"}
    ]
    },
    {
        "acno": 1003, "ac_type": "credit", "balance": 15000, "transactions": [
        {"to": 1001, "amount": 1500, "note": "ebill", "method": "g-pay"},
        {"to": 1002, "amount": 800, "note": "geto", "method": "neft"},
        {"to": 1000, "amount": 100, "note": "erchrge", "method": "phone-pay"}
    ]
    },
    {
        "acno": 1004, "ac_type": "savings", "balance": 50000, "transactions": [
        {"to": 1001, "amount": 500, "note": "ebill", "method": "g-pay"},
        {"to": 1002, "amount": 600, "note": "geto", "method": "neft"},
        {"to": 1003, "amount": 100, "note": "erchrge", "method": "phone-pay"}
    ]
    },

]

# for ac in accounts:
#     if ac["acno"]==1002:
#         print(ac)

# ac_details=[ac for ac in accounts if ac["acno"]==1002]
# print(ac_details)

#q4 prit all phone pay transactions

# all_transaction=[ac["transactions"] for ac in accounts ]
# print(all_transaction)
# p_trans=[tr for tlist in all_transaction for tr in tlist if tr["method"]=="phone-pay"]
# print(p_trans)
#
#
# #q4 prit all transactions where transaction amount > 500
# greater=[tr for tlist in all_transaction for tr in tlist if tr["amount"]>500]
# print(greater)
#
# #q5 crredit transactions of 1002
# cr_tranc=[tb for tlist in all_transaction for tb in tlist if tb["to"]==1002]
# print(cr_tranc)


#q6 aggregate transactions based on payment mode
pms={}
all_transaction=[ac["transactions"] for ac in accounts ]
transactions=[t for t_list in all_transaction for t in t_list]
for transaction in transactions:
    p_method=transaction["method"]
    amount=transaction["amount"]
    if p_method in pms:
        pms[p_method]+=amount
    else:
        pms[p_method]=amount

print(max(pms.items(),key=lambda itm:itm[1]))





# savings_ac=[ac["acno"] for ac in accounts if ac["ac_type"]=="savings"]
# print(savings_ac)
#
# accounts.sort(key=lambda ac:ac["balance"],reverse=True)
# print(accounts)

# transaction=[tranc for ac in accounts if tranc["transactions"]==1003]

