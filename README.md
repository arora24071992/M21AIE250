# Book Review System

## Overview

The Book Review System is a simple web application that allows users to add books along with their reviews. It's built using Flask, SQLite, and Vue.js, and styled with Bootstrap.

## Process Followed

1. **Setting up the Backend**:
    - Used Flask as the web framework.
    - SQLite was chosen for the database to store book details.
    - Created routes for the main page and adding books.

2. **Frontend**:
    - Used Vue.js for dynamic rendering of the book list.
    - Bootstrap was integrated for styling and responsiveness.
    - Custom CSS was added for additional styling.

3. **Docker Integration**:
    - Created a `Dockerfile` to containerize the application.
    - Used the `python:3.8-slim` image as the base.
    - Set up the working directory, copied the necessary files, and installed Flask.
    - Exposed port 5000 and set the command to run the Flask app.

## App Functionality

- **Add Books**: Users can add a book by providing its title, author, and an optional review.
- **View Books**: All added books are displayed in a list format with their respective reviews.

## Author

Roll Number: M21AIE250

---

## Setup and Run

To run the application:

1. Build the Docker image:
    ```bash
    docker build -t book-review-app .
    ```

2. Run the Docker container:
    ```bash
    docker run -p 5000:5000 book-review-app
    ```

3. Visit `http://localhost:5000` in your browser.

---





# M21AIE250
