# BlogCraft

### A Flask-Powered Blog & REST API

BlogCraft is a full-stack blog management application built with Python and Flask. It combines a server-rendered web interface with a REST API for programmatic access to blog posts.

The project demonstrates backend development with Flask, relational database management using SQLAlchemy ORM, CRUD operations, REST API development, form validation, CSRF protection, and API testing with Postman.

----------

## Application Preview

### Blog Homepage
<img width="1873" height="957" alt="Screen Shot 2026-09-03 at 14 27 54 p m" src="https://github.com/user-attachments/assets/b67b0d10-ff7c-472a-9757-369526dabe45" />



### Blog Post

<img width="1889" height="927" alt="Screen Shot 2026-09-03 at 14 51 47 p m" src="https://github.com/user-attachments/assets/3facb165-f6c3-4f00-9669-b82aec5ef574" />


### Create / Edit Post

<img width="1890" height="923" alt="Screen Shot 2026-09-03 at 14 54 08 p m" src="https://github.com/user-attachments/assets/4d45c5bf-d551-4363-a701-13a292749ad4" />


<img width="1885" height="907" alt="Screen Shot 2026-09-03 at 14 54 54 p m" src="https://github.com/user-attachments/assets/18ea283d-87f1-48e3-9176-6db98debb700" />


----------

## Features

### Web Application

-   Create new blog posts
    
-   View all blog posts
    
-   View individual blog posts
    
-   Edit existing posts
    
-   Delete blog posts
    
-   Rich text editing with CKEditor
    
-   Form validation with Flask-WTF
    
-   CSRF protection
    
-   Responsive interface using Bootstrap 5
    
-   SQLite relational database
    
-   SQLAlchemy ORM
    

### REST API

BlogCraft also provides a REST API for programmatic interaction with blog posts.

Method

Endpoint

Description

GET

`/api/posts`

Retrieve all blog posts

GET

`/api/posts/<post_id>`

Retrieve a single blog post

POST

`/api/posts/add-post`

Create a new blog post

PATCH

`/api/posts/<post_id>`

Update an existing blog post

DELETE

`/api/posts/delete-post/<post_id>`

Delete a blog post

API responses are returned in JSON format.

----------

## Technologies

### Backend

-   Python
    
-   Flask
    
-   Flask-SQLAlchemy
    
-   SQLAlchemy ORM
    
-   SQLite
    

### Web

-   Jinja2
    
-   HTML
    
-   CSS
    
-   Bootstrap 5
    
-   Flask-Bootstrap
    
-   CKEditor
    

### Forms & Security

-   Flask-WTF
    
-   WTForms
    
-   CSRF protection
    
-   Python-dotenv
    

### API Development

-   REST API
    
-   JSON
    
-   HTTP methods
    
-   Postman
    

### Development Tools

-   Git
    
-   GitHub
    
-   PyCharm
    

----------

## Application Architecture

The application uses Flask as the backend framework and SQLAlchemy as the ORM layer.

```text
                    ┌─────────────────────┐
                    │       Browser       │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │       Flask         │
                    │   Application       │
                    └───────┬─────┬───────┘
                            │     │
                 ┌──────────┘     └─────────────┐
                 ▼                              ▼
        ┌─────────────────┐           ┌─────────────────┐
        │ Jinja Templates │           │    REST API     │
        │   Web Interface │           │  JSON Responses │
        └─────────────────┘           └────────┬────────┘
                                               │
                                               ▼
                                    ┌─────────────────────┐
                                    │  SQLAlchemy ORM     │
                                    └──────────┬──────────┘
                                               │
                                               ▼
                                    ┌─────────────────────┐
                                    │   SQLite Database   │
                                    └─────────────────────┘

```

----------

## 🗄️ Database

BlogCraft uses SQLite with SQLAlchemy ORM.

The main database model is `BlogPost`.

### BlogPost fields

Field

Type

Description

`id`

Integer

Primary key

`title`

String

Blog post title

`subtitle`

String

Blog post subtitle

`date`

String

Publication date

`body`

Text

Blog post content

`author`

String

Author name

`img_url`

String

Blog post image URL

The `id` field is automatically generated as the primary key.

----------

# REST API

The REST API allows clients such as Postman or other applications to interact with the blog database without using the web interface.

## Get All Posts

### `GET /api/posts`

Returns all blog posts stored in the database.

### Example response

```json
[
    {
        "id": 1,
        "title": "Example Post",
        "subtitle": "An example blog post",
        "date": "September 03, 2026",
        "body": "This is an example blog post.",
        "author": "Emily Carter",
        "img_url": "https://example.com/image.jpg"
    }
]

```

----------

## Get a Single Post

### `GET /api/posts/<post_id>`

Returns a specific blog post using its database ID.

### Example

```text
GET /api/posts/5

```

### Example response

```json
{
    "id": 5,
    "title": "The Essential Role of Urban Trees",
    "subtitle": "Why cities need more trees than ever",
    "date": "September 03, 2026",
    "body": "Urban trees provide shade and improve the environment...",
    "author": "Emily Carter",
    "img_url": "https://example.com/tree.jpg"
}

```

----------

## Create a Post

### `POST /api/posts/add-post`

Creates a new blog post.

The current API accepts the post information through query parameters.

### Example

```text
/api/posts/add-post?title=The Hidden Life of Urban Trees&subtitle=How trees shape our cities&body=Urban trees provide shade and improve air quality.&author=Emily Carter&img_url=https://example.com/tree.jpg

```

### Example response

```json
{
    "response": {
        "Successfully Added": {
            "title": "The Hidden Life of Urban Trees",
            "subtitle": "How trees shape our cities",
            "date": "September 03, 2026",
            "body": "Urban trees provide shade and improve air quality.",
            "author": "Emily Carter",
            "img_url": "https://example.com/tree.jpg"
        }
    }
}

```

----------

## Update a Post

### `PATCH /api/posts/<post_id>`

Updates one or more fields of an existing blog post.

The current implementation supports partial updates using query parameters.

### Example

```text
/api/posts/5?title=The Essential Role of Urban Trees&subtitle=Why cities need more trees than ever

```

Only the provided fields are updated.

### Example response

```json
{
    "Response": {
        "Success Post Updated": {
            "title": "The Essential Role of Urban Trees",
            "subtitle": "Why cities need more trees than ever",
            "body": "Urban trees provide shade and improve air quality.",
            "author": "Emily Carter",
            "img_url": "https://example.com/tree.jpg"
        }
    }
}

```

----------

## Delete a Post

### `DELETE /api/posts/delete-post/<post_id>`

Deletes a blog post from the database.

The endpoint requires an API key.

### Example

```text
/api/posts/delete-post/5?api_key=YourSecretAPI

```

### Successful response

```json
{
    "response": {
        "Success": "The post was deleted."
    }
}

```

If the API key is incorrect, the API returns an error response.

> **Note:** The API key used in development should never be committed to the repository. Production applications should use a secure authentication and authorization mechanism.

----------

#  API Testing with Postman

The REST API was tested using Postman.

The Postman collection contains example requests for:

-   Retrieving all posts
    
-   Retrieving a single post
    
-   Creating a post
    
-   Updating a post
    
-   Deleting a post
    

### Postman Documentation

📖 **[Click to View BlogCraft API Documentation](https://documenter.getpostman.com/view/57498623/2sBYAvvWKQ)**

### Postman Collection

The exported Postman collection is included in this repository:

```text
/flask-blog-api/BlogCraft.postman_collection.json

```

You can import the collection into Postman to reproduce the API requests.

### Postman Screenshots

### Collections
<img width="215" height="147" alt="Screen Shot 2026-09-03 at 15 07 06 p m" src="https://github.com/user-attachments/assets/5d913577-a913-4764-ba4d-8568ee810684" />

### GET Request
<img width="1202" height="956" alt="Screen Shot 2026-09-03 at 15 08 35 p m -1" src="https://github.com/user-attachments/assets/e0f6f9ce-1932-49d1-823b-a42f5103bb17" />



### POST Request
<img width="1218" height="979" alt="Screen Shot 2026-09-03 at 15 50 29 p m" src="https://github.com/user-attachments/assets/e2f2424f-ea2b-439e-ad83-9e95fb453611" />


### PATCH Request
<img width="1217" height="971" alt="Screen Shot 2026-09-03 at 15 11 41 p m" src="https://github.com/user-attachments/assets/8594ed73-700b-40f2-9214-e832d8b077bb" />


### DELETE Request
<img width="1211" height="967" alt="Screen Shot 2026-09-03 at 15 13 35 p m" src="https://github.com/user-attachments/assets/d9d968f4-0033-427a-98eb-72a8402f9e21" />


----------

# Installation

## 1. Clone the repository

```bash
git clone https://github.com/alan24902/flask-blog-api
cd flask-blog-api

```

## 2. Create a virtual environment

```bash
python -m venv .venv

```

Activate it:

### macOS / Linux

```bash
source .venv/bin/activate

```

### Windows

```bash
.venv\Scripts\activate

```

## 3. Install dependencies

```bash
pip install -r requirements_3.13.txt

```

## 4. Configure environment variables

Create a `.env` file:

```text
SECRET_KEY=your-secret-key
API_KEY=your-api-key

```

A `.env.example` file is included as a template.

## 5. Run the application

```bash
python app.py

```

The application will run locally on:

```text
http://127.0.0.1:5003

```

----------

# 📁 Project Structure

```text
flask-blog-api/
│
├── app.py
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
│
├── static/
│   └── ...
│
├── templates/
│   ├── index.html
│   ├── post.html
│   ├── make-post.html
│   ├── about.html
│   └── contact.html
│
└── BlogCraft.postman_collection.json
    

```

----------

#  Project Purpose

This project was developed as a practical backend and web development project to strengthen skills in Python, Flask, relational databases, SQLAlchemy ORM, REST API development, and API testing.

The project combines a traditional server-rendered web application with a REST API, demonstrating how the same database can be accessed through both a web interface and programmatic API endpoints.

----------

#  Key Learning Outcomes

Through this project, I gained practical experience with:

-   Developing web applications with Flask
    
-   Designing relational database models
    
-   Using SQLAlchemy ORM for database operations
    
-   Implementing CRUD operations
    
-   Creating REST API endpoints
    
-   Working with HTTP methods including GET, POST, PATCH, and DELETE
    
-   Returning JSON responses
    
-   Handling request parameters
    
-   Implementing form validation
    
-   Protecting forms against CSRF attacks
    
-   Managing application secrets with environment variables
    
-   Testing APIs with Postman
    
-   Documenting APIs
    
-   Using Git and GitHub for version control
    

----------

## Future Improvements

Potential future improvements include:

-   Implementing JSON request bodies for POST and PATCH requests
    
-   Adding stronger API authentication and authorization
    
-   Improving API error handling and validation
    
-   Adding automated API tests
    
-   Adding pagination for large collections of posts
    
-   Separating the application into modules using Flask Blueprints
    
-   Adding production deployment configuration
    

----------

## Author

**Alan Quiñones**

Software Engineering Graduate | Python | Flask | SQL | Embedded Systems

GitHub: https://github.com/alan24902


