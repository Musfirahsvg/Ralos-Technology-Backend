from passlib.context import CryptContext

# Initialize the password context to use bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Hash the password '1234' (or any other password you want to hash)
hashed_password = pwd_context.hash("1234")

# Print the hashed password so you can copy it
print(hashed_password)
