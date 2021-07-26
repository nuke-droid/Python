
from hash import hash
import time
from os import strerror, system

starttime = time.time()

e = (IndexError)
h = hash()


str = input("Enter string to crack: ")

with open('pwd.txt') as f:
    content = f.readlines()


painbow = [[], []]


for i in content:

    j = i.splitlines()

    for k in j:

        l = h.hashgen(k)

        painbow.append([k, l])

ticker = 0

for i in range(len(painbow)):
    try:
        sub = painbow[i]
        #ystem('clear')

        

        if sub[1] == str:
            print(f"Cracked! Password: {sub[0]} Hash: {sub[1]}")
            ticker += 1
            endtime = time.time()
            print("--- %s seconds ---" % (time.time() - starttime))
            exit()

    except e:
        pass

if ticker <= 0:
    print("No corresponding hash found in database.")

endtime = time.time()

print(endtime - starttime)
