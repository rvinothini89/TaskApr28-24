import re
#Bangladesh number = +8801/00881 (Country code) followed by 1,5,6,7,8,9(any one digit) followed by 8 digits
mbl_number = "+8801712345678"
# pattern to validate bangladesh number
pattern = r'^(?:\+?88|0088)?01[15-9]\d{8}$'
if re.match(pattern,mbl_number):
    print("true")
else:
    print("false")