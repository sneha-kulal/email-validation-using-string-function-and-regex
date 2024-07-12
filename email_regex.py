
import re
email_condition =r"^[a-z]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
user = input("enter your mail: ")

if re.search(email_condition, user):
    print("Right email...")
else:
    print("Wrong email")