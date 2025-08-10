# 🎬 Movie Recommendation API

Welcome to the Movie Recommendation API repository! This project provides a RESTful API that delivers personalized movie recommendations based on user preferences. Whether you're building a movie discovery platform or integrating movie suggestions into your application, this API offers a robust solution.

---

## 🚀 Features

- **Personalized Recommendations**: Suggest movies tailored to individual user preferences.
- **Genre-Based Filtering**: Retrieve movies filtered by specific genres.
- **Random Movie Suggestions**: Get a random movie recommendation.
- **Search by Title**: Find movies by their title.
- **Movie Details**: Access detailed information about a specific movie.

---

## 🧱 Tech Stack

- **Backend**: Python 3.x
- **Framework**: FastAPI
- **Machine Learning**: Scikit-learn for recommendation algorithms
- **Data Source**: The Movie Database (TMDb) API


---

## 📁 Project Structure

The repository contains the following directories and files:

```
New_sample_dtkt_1/
└── app/
    ├── init.py
    ├── main.py
    ├── test_db_connection.py
    ├── controller/
    │   └── movie_controller.py
    ├── service/
    │   └── movie_service.py
    ├── models/
    │   └── models.py
    ├── db/
    │   └── database.py
    └── pycache/
```



---

## 📁 Folder Structure & Purpose

### **app/**  
Main Application Directory containing all the code following a layered architecture pattern.

### **controller/**  
- **File:** `movie_controller.py`  
- **Purpose:** Defines REST API routes and handles HTTP requests/responses, input validation, and calls service layer functions.

### **service/**  
- **File:** `movie_service.py`  
- **Purpose:** Contains business logic, data processing, transformations, validations, and database transactions.

### **models/**  
- **File:** `models.py`  
- **Purpose:** SQLAlchemy ORM models defining tables, relationships, constraints, and database schema.

### **db/**  
- **File:** `database.py`  
- **Purpose:** Database connectivity setup, engine and session management, and dependency injection for endpoints.

### **Core Application Files**

- **main.py**: Application entry point that initializes FastAPI app, database tables, registers routes, and defines the root health check endpoint.
- **test_db_connection.py**: Utility to test and validate MySQL database connectivity.

---

## 🔗 API Endpoints Detailed Explanation

### User Management

| Method | Endpoint  | Description                  |
|--------|-----------|------------------------------|
| POST   | `/users`  | Create a new user            |
| GET    | `/users`  | Get list of all users        |

### Movie Management

| Method | Endpoint   | Description                 |
|--------|------------|-----------------------------|
| POST   | `/movies`  | Add a new movie             |
| GET    | `/movies`  | Get all movies              |

### Rating System

| Method | Endpoint    | Description                 |
|--------|-------------|-----------------------------|
| POST   | `/ratings`  | Add a rating and review     |
| GET    | `/ratings`  | Get all ratings and reviews |

### System

| Method | Endpoint | Description            |
|--------|----------|------------------------|
| GET    | `/`      | API health check (Welcome message) |

---

## 💾 Database Schema

### Users Table

| Column   | Type    | Details               |
|----------|---------|-----------------------|
| id       | Integer | Primary Key, Auto-inc |
| username | String  | Unique, max 50 chars  |
| email    | String  | Unique, max 100 chars |

### Movies Table

| Column      | Type    | Details                |
|-------------|---------|------------------------|
| id          | Integer | Primary Key, Auto-inc  |
| movie_name  | String  | max 255 chars          |
| director    | String  | max 50 chars           |
| movie_genre | String  | max 20 chars           |
| description | Text    | Movie plot description |
| release_year| Integer | Year of release        |

### Ratings Table

| Column   | Type    | Details                           |
|----------|---------|---------------------------------|
| id       | Integer | Primary Key, Auto-inc            |
| user_id  | Integer | Foreign Key -> Users(id)         |
| movie_id | Integer | Foreign Key -> Movies(id)        |
| rating   | Integer | 1-5 rating (with DB constraint) |
| review   | Text    | User's written review            |

---

📝 **Conclusion**
This Movie Recommendation API follows clean architecture with separation of concerns:

Controllers: Handle HTTP requests and responses

Services: Implement business logic and data processing

Models: Define database schema and relationships

Database Layer: Manages persistence and connections


**Swagger document:** http://127.0.0.1:8000/docs



