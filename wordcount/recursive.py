pattern="ABACBB"
char_count={}
#    for char in pattern:
#     if char in char_count:
#         print("first recursive",char)
#         break
#     else:
#         char_count[char]=1
sec_char=[]
for char in pattern:
    if char in char_count:
        sec_char.append(char)
    else:
        char_count[char]=1
print(sec_char[1])
