from crackhash import crackhash
from hash import hash

decode = crackhash()
encode = hash()

def main():
   

    f= open('hashbrown.txt', 'r')

    file_contents = f.read()

    print(file_contents)

    answer  = None
    
    while answer != 'q' or None:

        answer = input("Please select from the following options:\n1. Encode/Hash\n2. Decode/Crack\nEnter 'q' to quit\n-> ")

        if answer == '1':
            encode.printhash()
        elif answer == '2':
            decode.main()


            


if __name__ == "__main__":

    main()

    
