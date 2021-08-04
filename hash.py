import hashlib


#custom hash class
class hash:
    
    #function which takes in plaintext value as strin str
    def hashgen(self, str, hashtype):
        hashtype = int(hashtype)    
        if hashtype == 1:
            result = hashlib.sha1(str.encode())
        elif hashtype == 2:
            result = hashlib.sha224(str.encode())
        elif hashtype == 3:
            result = hashlib.sha256(str.encode())
        elif hashtype == 4:
            result = hashlib.sha384(str.encode())
        elif hashtype == 5:
            result = hashlib.sha512(str.encode())
            
            
        if result != None:
            hashvalue = result.hexdigest()

        return hashvalue
    
    #private function for displaying plaintext hash when using class in script mode
    def list_hash_types(self):

        hashtypes = ['1. SHA-1', '2. SHA-224', '3. SHA-256', '4. SHA-384', '5. SHA-512']

        for h in range(len(hashtypes)):
            
            print(hashtypes[h])

    
    def printhash(self):
        str = input("Enter string to encode: ")
        self.list_hash_types()
        hashtype = input('Enter hashtype: ')

        print(self.hashgen(str, hashtype))

    def hashdetect(self, str):

        if (len(str)) == 40:
            hashtype = 'SHA1'
        elif (len(str)) == 56:
            hashtype = 'SHA224'
        elif (len(str)) == 64:
            hashtype = 'SHA256'
        elif (len(str)) == 96:
            hashtype = 'SHA384'
        elif (len(str)) == 128:
            hashtype = 'SHA512'
        else:
            hashtype = 'Null'

        return hashtype
        




    #main function for script mode
    def main(self):
        self._printhash()

        
    
#if statement for detecting if main is called. This dicates script behavior or module behavior
if __name__ == "__main__":
    h = hash()

    h.main()
        
