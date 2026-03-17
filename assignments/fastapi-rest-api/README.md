# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a RESTful API using FastAPI, including route handling, request validation, and JSON response formatting.

## 📝 Tasks

### 🛠️ Setup FastAPI Application

#### Description
Initialize a FastAPI app and create core endpoints for basic CRUD behavior using an in-memory data store.

#### Requirements
Completed program should:

- Install and import FastAPI and uvicorn.
- Create an app instance: `app = FastAPI()`.
- Add a root route `/` that returns a welcome JSON message.

### 🛠️ Create CRUD Endpoints for Users

#### Description
Implement endpoints to manage a simple in-memory list of users with basic create, read, update, and delete operations.

#### Requirements
Completed program should:

- Support `GET /users` returning all users.
- Support `GET /users/{user_id}` returning a single user or 404 if not found.
- Support `POST /users` to add a user with `name` and `email`.
- Support `PUT /users/{user_id}` to update user data.
- Support `DELETE /users/{user_id}` to remove a user.

### 🛠️ Input Validation and Error Handling

#### Description
Add request validation with Pydantic models and proper HTTP responses for invalid input or not found.

#### Requirements
Completed program should:

- Define Pydantic models for user creation and user response.
- Validate required fields and data formats.
- Return a `404` status code for missing resources and `400` for invalid requests.

### 🛠️ Run and Test the API

#### Description
Start the FastAPI app with uvicorn and test endpoints via HTTP client or browser.

#### Requirements
Completed program should:

- Include a `if __name__ == "__main__":` block to run `uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)`.
- Document example curl requests in comments.
