# from pydantic import BaseModel 

# class RegisterForm(BaseModel):
#     email: str
#     password: str
#     username: str
    
# class LoginForm(BaseModel):
#     email: str
#     password: str   
    
# class ChangePasswordData(BaseModel):
#     email: str
#     old_password: str
#     new_password: str




# json1
# {

#      "zero@gmail.com": {
#          "eamil": "zero@gmail.com",
#          "password": "1234",
#          "username": "zero"
#      }
#  } 




# json2
# {
#     "user@example.com": {
#         "email": "user@example.com",
#         "username": "user123",
#         "password": "$2b$12$H0XJ.9uh8N0YO1sVE1w8tuA0i2OhyY/TbiYQJRHvHqEzwC8C3kqZ2",  // hashed 'password123'
#         "workouts": {}
#     }
# }







from pydantic import BaseModel, EmailStr  # BaseModel for validation and EmailStr for strict email checking

# Model for user registration data
class RegisterForm(BaseModel):
    email: EmailStr  # Must be a valid email
    username: str    # Username as plain string
    password: str    # Plaintext password

# Model for user login
class LoginForm(BaseModel):
    email: EmailStr
    password: str

# Model for password change
class ChangePasswordData(BaseModel):
    email: EmailStr
    old_password: str
    new_password: str
