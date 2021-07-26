import hashlib



class hash:

    def hashgen(self, str):

        result = hashlib.sha256(str.encode())

        hashvalue = result.hexdigest()

        return hashvalue

    def _printhash(self):
        str = input("Enter string to encode: ")

        print(self.hashgen(str))


    def main(self):
        self._printhash()
        
    

if __name__ == "__main__":
    h = hash()

    h.main()
        
