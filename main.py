# # Import the FastAPI framework to create a web application
# from fastapi import FastAPI  

# # Import the workout routes from the `routes` package
# from routes.auth_routes import workout_routes  

# # Import the authentication routes from the `routes` package
# from routes.auth_routes import auth_router  

# # Import CORS Middleware to handle cross-origin requests
# from fastapi.middleware.cors import CORSMiddleware  
# # CORS (Cross-Origin Resource Sharing) is a security feature that controls which domains can communicate with your backend API.

# # Create an instance of the FastAPI application
# app = FastAPI()  

# # Add middleware for CORS to allow frontend communication with this backend
# app.add_middleware(
#     CORSMiddleware,  # Use CORS middleware
#     allow_origins=["http://localhost:3000"],  # Allow requests from frontend running on localhost:3000
#     allow_methods=["*"],  # Allow all HTTP methods (GET, POST, PUT, DELETE, etc.)
#     allow_headers=["*"],  # Allow all headers to be sent with the request
# )

# # Include the workout-related routes in the app
# app.include_router(
#     workout_routes,  # Use the imported workout_routes
#     prefix="/workouts",  # API endpoints for workouts will start with `/workouts`
#     tags=["Workouts"]  # Group these endpoints under the "Workouts" category in API documentation
# )

# # Include the authentication-related routes in the app
# app.include_router(
#     auth_router,  # Use the imported auth_router
#     prefix="/auth",  # API endpoints for authentication will start with `/auth`
#     tags=["Auth"]  # Group these endpoints under the "Auth" category in API documentation
# )

# # Define a simple test route at the root URL ("/")
# @app.get("/")  # This is a GET request for the root endpoint "/"
# def test():  # Define a function named `test`
#     return {"hello": "World"}  # Return a JSON response with a key "hello" and value "World"












from fastapi import FastAPI  # Import FastAPI app

# Import only the auth routes (no workouts anymore)
from routes.auth_routes import auth_router

# Import CORS middleware for frontend-backend communication
from fastapi.middleware.cors import CORSMiddleware

# Create FastAPI app instance
app = FastAPI()

# Allow frontend requests (from localhost:3000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Include only authentication routes now
app.include_router(auth_router, prefix="/auth", tags=["Auth"])

# Simple test route at root path
@app.get("/")
def test():
    return {"hello": "World"}
