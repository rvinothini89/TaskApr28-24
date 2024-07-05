import re
#US number = +1/001 (Country code) followed by 3 digit(area code) number followed by 7 digits
mbl_number = "+12124567890"
# pattern to validate usa number
pattern = r'^(?:\+?1|001)[0-9]{3}\d{7}$'
if re.match(pattern,mbl_number):
    print("true")
else:
    print("false")