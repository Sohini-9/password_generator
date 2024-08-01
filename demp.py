import bcrypt

password = b"thisismypassword"   #adding b converts the string to bytes
hashed = bcrypt.hashpw(password,bcrypt.gensalt())   #gensalt adds salt to the password

print(hashed)

entered_password = input('Enter password to login')
entered_password = bytes(entered_password,encoding='utf-8')
if bcrypt.checkpw(entered_password,hashed):   #checkpw converts the entered password into the hash value and then validates the hash value to check whther the entered password is correct
    print('Login successful')
else:
    print('Invalid password')



