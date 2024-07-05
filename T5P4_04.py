import re
# need to validate 16 digit alphanumeric password comprised of alphabets of upper case, lowercase,
# special characters, numbers
data = "cY51b%4HOjKv$8mF"
# pattern to validate 16 digit password
re1 = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{16}$'
pattern = re.compile(re1)
if re.match(pattern,data):
    print("true")
else:
    print("false")