
# Python 3 code to demonstrate
# SHA hash algorithms.

import hashlib
import os
import re


class hash:

    def hashgen(self, str):

        result = hashlib.sha256(str.encode())

        hashvalue = result.hexdigest()

        return hashvalue

    def printhash(self):
        str = input("Enter string to encode: ")

        print(self.hashgen(str))
