username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "admin123":
    print("Login successful")
else:
    print("Invalid credentials")

#❌ Why this is insecure

#Password is hardcoded

#Password is in plain text

#Anyone reading code knows the password

#No protection against brute force