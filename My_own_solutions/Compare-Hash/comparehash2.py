# code to compare  hashstrings
# This is an improved version which
# prompts for the hash strings so
# that the user doesn't have to 
# edit the Python code each time
# in order to use it
# 

SHA256sum = input("Please paste SHA256sum from download site: ")
hash = input("Please paste hash from downloaded file: ")
print(SHA256sum.lower() == hash.lower())
