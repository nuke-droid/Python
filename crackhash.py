
from hash import hash
import time
from os import strerror, system

#Start time is recorded and stored for duration calulation
starttime = time.time()

#List of exceptions is created
e = (IndexError)

#hash object is created as h
h = hash()

#prompt for string user input
str = input("Enter string to crack: ")
hashType = h.hashdetect(str)

print(f'{hashType} hash type detected!')
detectedHash = None
if hashType == 'SHA1':
    detectedHash = 1
elif hashType == 'SHA224':
    detectedHash = 2
elif hashType == 'SHA256':
    detectedHash = 3
elif hashType == 'SHA384':
    detectedHash = 4
elif hashType == 'SHA512':
    detectedHash = 5

#import text file with list of commond passwords
with open('pwd.txt') as f:
    content = f.readlines()

#instantiates empty 2 dimensional list
painbow = [[], []]

#loops through text file to separate inputs
for i in content:
    #splits each items by newline
    j = i.splitlines()
    
    #loop stores split items into plaintext and hash into two-dimensional list respectively
    for k in j:



        l = h.hashgen(k, detectedHash)

        painbow.append([k, l])
#counter serves to provide message in the case that there is no corresponding plaintext value found for the input hash
ticker = 0

for i in range(len(painbow)):
    try:
        sub = painbow[i]
        #ystem('clear')

        
        #if value is found in hashses stored in memory, corresponding plaintext value is displayed and program exit
        if sub[1] == str:
            print(f"Cracked! Password: {sub[0]} Hash: {sub[1]}")
            ticker += 1
            endtime = time.time()

            print("--- %s milliseconds ---" % (time.time() - starttime))

            exit()
    
    except e:
        pass

if ticker <= 0:
    print("No corresponding hash found in database.")
    endtime = time.time()
#Total runtime/duration
print(endtime - starttime)
