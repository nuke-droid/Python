import hashlib



class hash:

    def hashgen(self, str):

        result = hashlib.sha256(str.encode())

        hashvalue = result.hexdigest()

        return hashvalue

    def _printhash(self):
        str = input("Enter string to encode: ")

        print(self.hashgen(str))

    def phash(self):
        self._printhash()

    

h = hash()

h.phash()
