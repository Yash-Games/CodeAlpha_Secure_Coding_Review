import hashlib

stored_password_hash = hashlib.sha256("admin123".encode()).hexdigest()

user_password = input("Enter password: ")
hashed_input = hashlib.sha256(user_password.encode()).hexdigest()

if hashed_input == stored_password_hash:
    print("Login successful")
else:
    print("Invalid credentials")


# What improved

#Password is hashed

#Plain text password comparison removed

#Reduced risk of credential exposure