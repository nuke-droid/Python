
from hash import hash

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


for i in range(len(painbow)):
    try:
        sub = painbow[i]

        if sub[1] == str:
            print(f"Cracked! Password: {sub[0]} Hash: {sub[1]}")

    except e:
        pass
