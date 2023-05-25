# your code goes here!


import re

class EmailAddressParser:
    def __init__(self, email_address):
        self.email_address = email_address

    def parse(self):
        pattern = r"\b[A-Za-z0-9.]+@[A-Za-z0-9.-]+\.[A-Za-z]{3,}\b"
        email = re.findall(pattern, self.email_address)

        email.sort()

        return email


  