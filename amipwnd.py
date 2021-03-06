'''

    Description: Easy and safer way to check whether your password is exposed in data breaches.
                 Clone my code run in your system
                 Password is not shared with the api. First 5 characters of hash used to check in hash repository.
                 Utilizing api of https://api.pwnedpasswords.com/
'''
import requests
import hashlib
import sys

class Amipwned():
    def __init__(self,passwd):
        self.passwd = passwd
    def pwdcheck(self):
        hashes = hashlib.sha1(self.passwd.encode('utf-8')).hexdigest().upper()
        h5,hl = hashes[:5],hashes[5:]
        url = requests.get("https://api.pwnedpasswords.com/range/"+h5)
        if url.status_code == 200:
            print("Connected to pwned database...")
            hash_list = [hash_elem.split(":") for hash_elem in url.text.splitlines()]
            for k,v in hash_list:
                if k == hl:
                    return f"Your password found in a data breach: {v} times! Feel free to change the password to protect your data.." 
                elif len(hash_list) == hash_list.index([k,v])+1:
                    return f"No worries!! your data is not compromised!  you are safe"
        else:
            print("Not connected!!")

A=Amipwned(sys.argv[1])
print(A.pwdcheck())
