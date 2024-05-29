<h1>FastAPI with MongoDB Demo</h1>
    <p>This project demonstrates a RESTful API built with FastAPI, a modern web framework for building APIs with Python, and MongoDB, a NoSQL database. The API allows users to perform CRUD (Create, Read, Update, Delete) operations on user records stored in a MongoDB database.</p>
    
<h2>Features</h2>
    <ul>
        <li><strong>Create User:</strong> Add a new user to the database with a unique name and email.</li>
        <li><strong>Read Users:</strong> Retrieve a list of all users stored in the database.</li>
        <li><strong>Read Users by Name:</strong> Search for users by their name.</li>
        <li><strong>Update User by Name:</strong> Update the details of a user based on their name.</li>
        <li><strong>Delete User by Name:</strong> Delete a user from the database by their name.</li>
    </ul>
    
<h2>Prerequisites</h2>
    <p>Before running the application, ensure you have the following installed:</p>
    <ul>
        <li>Python 3.x</li>
        <li>MongoDB</li>
        <li>FastAPI and dependencies (install via <code>pip install fastapi[all]</code>)</li>
        <li>Pydantic (installed automatically with FastAPI)</li>
        <li>pymongo (install via <code>pip install pymongo</code>)</li>
        <li>uvicorn (install via <code>pip install uvicorn</code>)</li>
    </ul>
