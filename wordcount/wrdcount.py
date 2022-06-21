# text="hello hai hello"
# words=text.split(" ")
# # print(len(words))
# # print(words)
# wordcount={}
#
# for w in words:
#     if w in wordcount:
#         wordcount[w]+=1
#     else:
#         wordcount[w]=1
# print(wordcount)

word_count={"a":2,"b":3,"c":5,"d":6}
# wr_count=word_count.items()
# print(sorted(wr_count,key=lambda item:item[1],reverse=True))

print(min(word_count.items(),key=lambda l:l[1]))