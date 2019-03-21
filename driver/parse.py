f1 = open("new.txt", 'r')
f2 = open('new_title.txt', 'w')
lines = f1.readlines()
i=0
for line in lines:
    if i%2 == 0:
        line=line[6:16]
        line='https://www.imdb.com/title'+line+'/reviews?ref_=tt_ql_3'
        f2.write(line)
        f2.write('\n')
    i=i+1
line = f1.readline()
#print(line)

#print(my[6:16])

f1.close()
f2.close()