# import json
# from fastapi import APIRouter, HTTPException

# from models.auth_models import LoginForm, RegisterForm


# auth_router = APIRouter()

# def get_all_users():
#     with open("./fake_db/users.json", "r") as file:
#         return json.load(file)
        

# def save_users(new_users):
#     with open("./fake_db/users.json", "w") as file:
#         file.write(json.dumps(new_users, indent=4))    #difference between dumps and dump
        
        
# @auth_router.post("/register")
# def register(register_data: RegisterForm):
    
#     all_users = get_all_users()
#     email = register_data.email
    
    
#     if email in all_users:
#         raise HTTPException(409, "User already exists")
    
#     # new_user={
#     #     "email": register_data.email,
#     #     "username":register_data.username,
#     #     "password": register_data.password,    
#     # }
    
#     new_user = register_data.model_dump()
#     new_user [ "workouts"] = {}
    
#     all_users[email] = new_user
    
#     save_users(all_users)
#     return new_user
    


# @auth_router.post("/login")
# def login(login_data: LoginForm):
    
#     all_users = get_all_users()
#     email = login_data.email

#     if email not in all_users:
#         raise HTTPException(401, "Invalid Credentials")
    
#     if all_users[email]["password"] != login_data.password:
#         raise HTTPException(401, "Invalid Credentials")
    

#     return all_users[email]

# @app.post("/auth/change-password")
# def change_password(data: ChangePasswordData):
#     user = users_db.get(data.email)
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")

#     if not pwd_context.verify(data.old_password, user["password"]):
#         raise HTTPException(status_code=401, detail="Old password is incorrect")

#     if pwd_context.verify(data.new_password, user["password"]):
#         raise HTTPException(status_code=400, detail="New password cannot be the same as the old password")

#     users_db[data.email]["password"] = pwd_context.hash(data.new_password)
#     return {"message": "Password changed successfully"}


    # if email in all_users:
    #     #check if password is correct
    #     if all_users[email]["password"] == login_data.password:
    #         return all_users[email]
    #     else: HTTPException(401, "Invalid Credentials")
    # else:
    #     raise HTTPException(401, "Invalid Credentials")
    # return{}  
    
    
    
    
    
    
    
    
# import json  # Import the JSON module to handle JSON data
# from fastapi import APIRouter, HTTPException  # Import FastAPI components for routing and error handling
# from models.auth_models import LoginForm, RegisterForm, ChangePasswordData  # Import Pydantic models for validation
# from passlib.context import CryptContext  # Import passlib for password hashing

# auth_router = APIRouter()  # Create an instance of APIRouter for handling authentication routes
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")  # Initialize password context for hashing

# def get_all_users():
#     with open("./fake_db/users.json", "r") as file:  # Open the users JSON file for reading
#         return json.load(file)  # Load and return the JSON data as a Python dictionary

# def save_users(new_users):
#     with open("./fake_db/users.json", "w") as file:  # Open the users JSON file for writing
#         file.write(json.dumps(new_users, indent=4))  # Write the updated user data back to the file in a pretty format

# @auth_router.post("/register")  # Define a POST endpoint for user registration
# def register(register_data: RegisterForm):  # Accept registration data as a RegisterForm model
#     all_users = get_all_users()  # Retrieve all existing users
#     email = register_data.email  # Extract the email from the registration data

#     if email in all_users:  # Check if the email already exists
#         raise HTTPException(409, "User  already exists")  # Raise a conflict error if the user exists

#     # Highlighted change: Use dict() to convert Pydantic model to a dictionary
#     new_user = register_data.dict()  # Convert the Pydantic model to a dictionary
#     new_user["workouts"] = {}  # Initialize an empty workouts dictionary for the new user

#     all_users[email] = new_user  # Add the new user to the all_users dictionary
#     save_users(all_users)  # Save the updated users back to the JSON file
#     return new_user  # Return the newly registered user data

# @auth_router.post("/login")  # Define a POST endpoint for user login
# def login(login_data: LoginForm):  # Accept login data as a LoginForm model
#     all_users = get_all_users()  # Retrieve all existing users
#     email = login_data.email  # Extract the email from the login data

#     if email not in all_users:  # Check if the email exists in the users
#         raise HTTPException(401, "Invalid Credentials")  # Raise an unauthorized error if the user does not exist

#     if all_users[email]["password"] != login_data.password:  # Check if the password matches
#         raise HTTPException(401, "Invalid Credentials")  # Raise an unauthorized error if the password is incorrect

#     return all_users[email]  # Return the user data if login is successful

# @auth_router.post("/change-password")  # Define a POST endpoint for changing the password
# def change_password(data: ChangePasswordData):  # Accept password change data as a ChangePasswordData model
#     all_users = get_all_users()  # Retrieve all existing users
#     user = all_users.get(data.email)  # Get the user by email from the data
#     if not user:  # Check if the user exists
#         raise HTTPException(status_code=404, detail="User  not found")  # Raise a not found error if the user does not exist

#     if not pwd_context.verify(data.old_password, user["password"]):  # Verify the old password
#         raise HTTPException(status_code=401, detail="Old password is incorrect")  # Raise an unauthorized error if the old password is incorrect

#     if pwd_context.verify(data.new_password, user["password"]):  # Check if the new password is the same as the old one
#         raise HTTPException(status_code=400, detail="New password cannot be the same as the old password")  # Raise a bad request error if they are the same

#     # Highlighted change: Hash the new password before saving
#     all_users[data.email]["password"] = pwd_context.hash(data.new_password)  # Hash the new password and update the user data
#     save_users(all_users)  # Save the updated users back to the JSON file
#     return {"message": "Password changed successfully"}  # Return a success message  





import json
import os  # To work with JSON file storage
from fastapi import APIRouter, HTTPException  # For API routing and error handling
from passlib.context import CryptContext  # To securely hash and verify passwords

# Import the models (schemas) for input validation
from models.auth_models import LoginForm, RegisterForm, ChangePasswordData

# Create an APIRouter instance to define auth-related endpoints
auth_router = APIRouter()

# Set up password hashing context using bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Function to load all users from the JSON file (our fake database)
def get_all_users():
    
    base_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory of this script
    file_path = os.path.join(base_dir, '..', 'fake_db', 'users.json')     
    
    try:
        with open(file_path, "r") as file:
            return json.load(file)  # Load users if the file is not empty
    except json.JSONDecodeError:
        return {}  # Return an empty dictionary if the file is empty

# Function to save updated users back to the JSON file
def save_users(new_users):
    base_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory of this script
    file_path = os.path.join(base_dir, '..', 'fake_db', 'users.json')   
    with open(file_path, "w") as file:
        json.dump(new_users, file, indent=4)

@auth_router.post("/register")
def register(register_data: RegisterForm):
    all_users = get_all_users()  # Load existing users
    email = register_data.email

    # Check if the email already exists in the databaseSSSSS
    if email in all_users:
        raise HTTPException(409, "User already exists")

    # Hash the password before saving
    hashed_password = pwd_context.hash(register_data.password)

    # Convert the RegisterForm data into a dictionary
    new_user = register_data.model_dump()
    new_user["password"] = hashed_password  # Store the hashed password

    # Save the new user
    all_users[email] = new_user
    save_users(all_users)

    return {"message": "User registered successfully"}

# Login endpoint
@auth_router.post("/login")
def login(login_data: LoginForm):
    all_users = get_all_users()  # Load all users
    email = login_data.email

    # Check if the email exists
    if email not in all_users:
        raise HTTPException(401, "Invalid credentials")

    # Verify the entered password with the hashed password
    if not pwd_context.verify(login_data.password, all_users[email]["password"]):
        raise HTTPException(401, "Invalid credentials")

    # Return success message and user data (excluding password is recommended)
    return {"message": "Login successful", "user": all_users[email]}

# Change password endpoint
@auth_router.post("/change-password")
def change_password(data: ChangePasswordData):
    all_users = get_all_users()  # Load user data

    # Get user info based on email
    user = all_users.get(data.email)
    if not user:
        raise HTTPException(404, detail="User not found")

    # Verify old password
    if not pwd_context.verify(data.old_password, user["password"]):
        raise HTTPException(401, detail="Old password is incorrect")

    # Check if new password is the same as the old one
    if data.old_password == data.new_password:
        raise HTTPException(400, detail="New password cannot be the same as the old password")

    # Hash and update the new password
    user["password"] = pwd_context.hash(data.new_password)
    save_users(all_users)  # Save changes

    return {"message": "Password changed successfully"}








# # Function to load all users from the JSON file (our fake database)
# def get_all_users():
#     try:
#         with open("./fake_db/users.json", "r") as file:
#             return json.load(file)  # Load users if the file is not empty
#     except json.JSONDecodeError:
#         return {}  # Return an empty dictionary if the file is empty

# # Function to save updated users back to the JSON file
# def save_users(new_users):
#     with open("./fake_db/users.json", "w") as file:
#         json.dump(new_users, file, indent=4)

# @auth_router.post("/register")
# def register(register_data: RegisterForm):
#     all_users = get_all_users()  # Load existing users
#     email = register_data.email

#     # Check if the email already exists in the database
#     if email in all_users:
#         raise HTTPException(409, "User already exists")

#     # Hash the password before saving
#     hashed_password = pwd_context.hash(register_data.password)

#     # Convert the RegisterForm data into a dictionary
#     new_user = register_data.model_dump()
#     new_user["password"] = hashed_password  # Store the hashed password

#     # Save the new user
#     all_users[email] = new_user
#     save_users(all_users)

#     return {"message": "User registered successfully"}
