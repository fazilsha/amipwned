'''

    Description: Easy and safer to check wheather your password is exposed or not.
                 Utilizing api of https://api.pwnedpasswords.com/
'''
import requests
import hashlib

class Amipwned():
    def __init__(self,passwd):
        self.passwd = passwd
    def pwdcheck(self):
        hashes = hashlib.sha1(self.passwd.encode('utf-8')).hexdigest().upper()
        h5,hl = hashes[:5],hashes[5:]
        url = requests.get("https://api.pwnedpasswords.com/range/"+h5)
        if url.status_code == 200:
            print("Connected!")
            hash_list = (hash_elem.split(":") for hash_elem in url.text.splitlines())
            for k,v in hash_list:
                if k == hl:
                    return f"Your password found in a data breach: {v} times! Feel free to change the password to protect your data.."
        else:
            print("Not connected!!")

A=Amipwned("hello")
A.pwdcheck()
