import re 
email = "rvinothiniblr@gmail.com"
#Pattern to validate email address
pattern = r'^[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,6}$'
if re.match(pattern,email):
    print("true")
else:
    print("false")