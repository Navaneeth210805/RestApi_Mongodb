FastAPI with MongoDB Demo
This project demonstrates a RESTful API built with FastAPI, a modern web framework for building APIs with Python, and MongoDB, a NoSQL database. The API allows users to perform CRUD (Create, Read, Update, Delete) operations on user records stored in a MongoDB database.

Features
Create User: Add a new user to the database with a unique name and email.
Read Users: Retrieve a list of all users stored in the database.
Read Users by Name: Search for users by their name.
Update User by Name: Update the details of a user based on their name.
Delete User by Name: Delete a user from the database by their name.
Prerequisites
Before running the application, ensure you have the following installed:

Python 3.x
MongoDB
FastAPI and dependencies (install via pip install fastapi)
Pydantic (installed automatically with FastAPI) 
pymongo (install via pip install pymongo)
uvicorn (install via pip install uvicorn)