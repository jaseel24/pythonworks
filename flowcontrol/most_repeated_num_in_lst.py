List = [2, 1, 2, 2, 1, 3]
counter = 0
greatestoccurednum = 0
for i in List:
        curr_frequency = List.count(i)
        # print(List.count(i))
        if (curr_frequency > counter):
            counter = curr_frequency
            greatestoccurednum=i
print(greatestoccurednum)



