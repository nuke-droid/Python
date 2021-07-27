import hashlib


#custom hash class
class hash:
    
    #function which takes in plaintext value as strin str
    def hashgen(self, str):

        result = hashlib.sha256(str.encode())

        hashvalue = result.hexdigest()

        return hashvalue
    
    #private function for displaying plaintext hash when using class in script mode
    def _printhash(self):
        str = input("Enter string to encode: ")

        print(self.hashgen(str))

    #main function for script mode
    def main(self):
        self._printhash()
        
    
#if statement for detecting if main is called. This dicates script behavior or module behavior
if __name__ == "__main__":
    h = hash()

    h.main()
        
